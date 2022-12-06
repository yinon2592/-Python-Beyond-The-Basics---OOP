import  json
# {"back_up_day_limit": 21, "backup_dir": "/mnt/alpah/db_backups",
#  "backup_retrieval_dir": "/mnt/alpah/db_backups/backup_retrieval", "read_db": "mysql_managed_db",
#  "tarfile_match_pattern": "\\d\\d\\d\\d-\\d\\d-\\d\\d\\_fiba\\.tar$", "temp_backup_dir": "/mnt/alpah/db_backups/temp"}
# with open('backup_config.json') as fh:
#     conf = json.load(fh)
#
# print("\ncontent is : \n",conf) ; print("\ntype is : \n", type(conf))

with open('backup_config.json', 'rb') as fh:
    conf = json.load(fh)
print(conf)
conf['new_key'] = 5.00005
with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ': '))
# my_json_list = {'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}
# x = json.dumps(my_json_list)
# print("x content is : ", x, "\nx type is : ", type(x))
# my_struct = json.loads(x)
# print("my_struct is from type :", type(my_struct))
# for key, elements in my_struct.items():
#     print(key)
#     for elem in elements:
#         print("\t",elem)
