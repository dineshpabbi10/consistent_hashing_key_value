## Output

```bash
$ python consistant_hashing.py 
2025-03-04 00:47:21 [INFO] Adding server = server1
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Adding server = server2
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Adding server = server3
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Adding server = server4
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Adding server = server5
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Found servers = ('server4', 'server5', 'server2')
2025-03-04 00:47:21 [INFO] Key = key1 added to =['server4', 'server5', 'server2'] nodes
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Key = key2 added to =['server2', 'server5', 'server5'] nodes
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server1', 'server3')
2025-03-04 00:47:21 [INFO] Key = key3 added to =['server5', 'server1', 'server3'] nodes
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server4', 'server5')
2025-03-04 00:47:21 [INFO] Key = key4 added to =['server5', 'server4', 'server5'] nodes
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Key = key5 added to =['server3', 'server5', 'server4'] nodes
2025-03-04 00:47:21 [INFO] Found servers = ('server4', 'server5', 'server2')
2025-03-04 00:47:21 [INFO] Key = key1 fetched from server4
value1
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Key = key2 fetched from server2
value2
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server1', 'server3')
2025-03-04 00:47:21 [INFO] Key = key3 fetched from server5
value3
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server4', 'server5')
2025-03-04 00:47:21 [INFO] Key = key4 fetched from server5
value4
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Key = key5 fetched from server3
value5
2025-03-04 00:47:21 [INFO] Adding server = server6
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Reassigning key = key3 to ['server5', 'server6', 'server3'] nodes from server1
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Reassigning key = key1 to ['server6', 'server5', 'server4'] nodes from server2
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Reassigning key = key4 to ['server6', 'server4', 'server4'] nodes from server5
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Key = key1 fetched from server6
value1
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Key = key2 fetched from server2
value2
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Key = key3 fetched from server5
value3
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Key = key4 fetched from server6
value4
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Key = key5 fetched from server3
value5
2025-03-04 00:47:21 [INFO] Deleting server = server1
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server3')
2025-03-04 00:47:21 [INFO] Reassigning key = key5 to ['server3', 'server5', 'server3'] nodes from server4
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server2', 'server5', 'server5')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server5', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Deleting server = server2
2025-03-04 00:47:21 [INFO] Syncing keys...
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server4')
2025-03-04 00:47:21 [INFO] Reassigning key = key3 to ['server5', 'server6', 'server4'] nodes from server3
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server4', 'server3')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server4', 'server3', 'server6')
2025-03-04 00:47:21 [INFO] Reassigning key = key2 to ['server4', 'server3', 'server6'] nodes from server5
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server4', 'server3')
2025-03-04 00:47:21 [INFO] Reassigning key = key5 to ['server3', 'server4', 'server3'] nodes from server5
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Found servers = ('server4', 'server3', 'server6')
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Key = key1 fetched from server6
value1
2025-03-04 00:47:21 [INFO] Found servers = ('server4', 'server3', 'server6')
2025-03-04 00:47:21 [INFO] Key = key2 fetched from server4
value2
2025-03-04 00:47:21 [INFO] Found servers = ('server5', 'server6', 'server4')
2025-03-04 00:47:21 [INFO] Key = key3 fetched from server5
value3
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server4', 'server4')
2025-03-04 00:47:21 [INFO] Key = key4 fetched from server6
value4
2025-03-04 00:47:21 [INFO] Found servers = ('server3', 'server4', 'server3')
2025-03-04 00:47:21 [INFO] Key = key5 fetched from server3
value5
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
2025-03-04 00:47:21 [INFO] Deleted key = key1 from ['server6', 'server5', 'server4']
2025-03-04 00:47:21 [INFO] Found servers = ('server6', 'server5', 'server4')
Traceback (most recent call last):
  File "C:\Projects\system_design_impl\consistant_hashing.py", line 253, in <module>
    print(ch.get_key("key1"))  # Exception
  File "C:\Projects\system_design_impl\consistant_hashing.py", line 194, in get_key
    raise Exception("No value found for key")
Exception: No value found for key
```
