import hashlib
import bisect
import logging
from logging import getLogger

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = getLogger(__name__)

class ConsistentHashing:
    def __init__(self, replicas:int=3):
        self.replicas:int = replicas
        self.servers:dict = {}
        self.ring = []
        self.replica_to_server = {}

    def get_hash(self,s:str):
        """
        Description
        -------------
        Calculates the hash value for a given string.

        Parameters
        ----------
        s: str
        The string for which the hash value needs to be calculated.

        Returns
        -------
        int : int value of hexadecimal representation
        """
        return int(hashlib.md5(s.encode('utf-8')).hexdigest(),16)
    
    def get_server_id_for_hash(self,hash:int):
        """
        Description
        -------------
        Finds the server id for a given hash value.

        Parameters
        ----------
        hash: int
        The hash value for which the server id needs to be found.

        Returns
        -------
        tuple : tuple of server ids
        """
        # Find index of replica for hashkey
        index =  bisect.bisect(self.ring,hash)

        # if index matches end of ring, move to index 0 since ring is circular
        if(index == len(self.ring)):
            index = 0

        # Get prev index for replication of data on other node
        prev_index = index - 2 if index > 1 else len(self.ring) - 2
        
        # Next index for replication of data on other node
        next_index = index+2 if index < len(self.ring) - 2 else 0

        servers =  (self.replica_to_server[self.ring[index]],
                self.replica_to_server[self.ring[prev_index]], # replicate data across prev node
                self.replica_to_server[self.ring[next_index]]) # replicate data across next node

        logger.info(f"Found servers = {servers}")
        return servers
    
    def add_server(self,server_key:str):
        """
        Description
        -------------
        Adds a new server to the consistent hashing ring.

        Parameters
        ----------
        server_key: str
        The unique identifier for the new server.
        """
        logger.info(f"Adding server = {server_key}")
        if(server_key in self.servers):
            raise Exception("Server already exists")
        
        # Initialize server with empty dictionary
        self.servers[server_key] = {}

        # Add virtual nodes / replicas
        for i in range(self.replicas):
            hash_val = self.get_hash(f"{server_key}_{i}")
            self.replica_to_server[hash_val] = server_key
            bisect.insort(self.ring,hash_val)

        logger.info("Syncing keys...")
        # Sync Keys
        self.sync_keys()
    

    def delete_server(self,server_key:str):
        """
        Description
        -------------
        Deletes a server from the consistent hashing ring.

        Parameters
        ----------
        server_key: str
        """
        logger.info(f"Deleting server = {server_key}")
        if(server_key not in self.servers):
            raise Exception("Server does not exists")
        
        # Delete node
        del self.servers[server_key]

        # Delete virtual nodes / replicas
        for i in range(self.replicas):
            hash_val = self.get_hash(f"{server_key}_{i}")
            index = bisect.bisect_left(self.ring,hash_val)
            del self.ring[index]

        logger.info("Syncing keys...")
        # Sync Keys
        self.sync_keys()
    
    def sync_keys(self):
        """
        Description
        -------------
        Syncs keys across all servers.
        """
        # For all servers
        for server in self.servers: 
            # And for all keys in each server
            keys = list(self.servers[server].keys())
            for key in keys:
                key_hash = self.get_hash(key)
                 # Find all server key should exist including replica nodes
                s1,s2,s3 = self.get_server_id_for_hash(key_hash)
                # if current server does not match any server, remove from current and add key to all new servers
                if( server not in {s1,s2,s3} ): 
                    logger.info(f"Reassigning key = {key} to {[s1,s2,s3]} nodes from {server}")
                    self.servers[s1][key] = self.servers[server][key]
                    self.servers[s2][key] = self.servers[server][key]
                    self.servers[s3][key] = self.servers[server][key]
                    del self.servers[server][key]
    
    def put_key(self,key:str,value:str):
        """
        Description
        -------------
        Adds a key-value pair to the consistent hashing ring.

        Parameters
        ----------
        key: str
        The unique identifier for the key.

        value: str
        The value associated with the key.
        """
        hash_key = self.get_hash(key)
        s1,s2,s3 = self.get_server_id_for_hash(hash_key)
        
        self.servers[s1][key] = value
        self.servers[s2][key] = value
        self.servers[s3][key] = value
        logger.info(f"Key = {key} added to ={[s1,s2,s3]} nodes")

    def get_key(self,key:str):
        """
        Desctiption
        -----------
        Retrieves the value associated with a given key from the consistent hashing ring.

        Parameters
        ----------
        key: str

        Returns
        str : value associated with key
        """
        hash_key = self.get_hash(key)
        s1,s2,s3 = self.get_server_id_for_hash(hash_key)
        
        for server in [s1,s2,s3]:
            if(key in self.servers[server]):
                logger.info(f"Key = {key} fetched from {server}")
                return self.servers[server][key]
        
        raise Exception("No value found for key")
    
    def delete_key(self,key:str):
        """
        Description
        -----------
        Deletes a key-value pair from the consistent hashing ring.

        Parameters
        ----------
        key: str
        The unique identifier for the key.
        """
        hash_key = self.get_hash(key)
        s1,s2,s3 = self.get_server_id_for_hash(hash_key)
        
        for server in [s1,s2,s3]:
            del self.servers[server][key]
        
        logger.info(f"Deleted key = {key} from {[s1,s2,s3]}")


if __name__ == "__main__":
    ch = ConsistentHashing(replicas=10)
    ch.add_server("server1")
    ch.add_server("server2")
    ch.add_server("server3")
    ch.add_server("server4")
    ch.add_server("server5")

    ch.put_key("key1", "value1")
    ch.put_key("key2", "value2")
    ch.put_key("key3", "value3")
    ch.put_key("key4", "value4")
    ch.put_key("key5", "value5")

    print(ch.get_key("key1"))  # Output: value1
    print(ch.get_key("key2"))  # Output: value2
    print(ch.get_key("key3"))  # Output: value3
    print(ch.get_key("key4"))  # Output: value4
    print(ch.get_key("key5"))  # Output: value5

    ch.add_server("server6")
    print(ch.get_key("key1"))  # Output: value1
    print(ch.get_key("key2"))  # Output: value2
    print(ch.get_key("key3"))  # Output: value3
    print(ch.get_key("key4"))  # Output: value4
    print(ch.get_key("key5"))  # Output: value5

    ch.delete_server("server1")
    ch.delete_server("server2")

    print(ch.get_key("key1"))  # Output: value1
    print(ch.get_key("key2"))  # Output: value2
    print(ch.get_key("key3"))  # Output: value3
    print(ch.get_key("key4"))  # Output: value4
    print(ch.get_key("key5"))  # Output: value5

    ch.delete_key("key1")
    print(ch.get_key("key1"))  # Exception
