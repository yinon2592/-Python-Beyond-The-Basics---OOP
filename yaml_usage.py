import yaml
import json

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_list = [1, 2, 3, 4, 5]
# my_tuple = ('x', 'y', 'z')
#
# loaded_yaml = yaml.dump(my_dict, default_flow_style=False)
# print(loaded_yaml)
# print(yaml.dump(my_list, default_flow_style=False)
# print(yaml.dump(my_tuple, default_flow_style=False)
# white space defer diffrent objects
# my_obj = {
#     [1, 2, 3, 4, 5],
#     {'a': 1, 'b': 2, 'c': 3},
#     [
#         {'x': 98, 'y': 99, 'z': 100},
#         3,
#         4
#     ],
#     {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# }
# print(yaml.dump(my_obj, default_flow_style=False))

# not like pickle and json, load/dump will work with file handler or string (no need of loads/dumps)
# with open('app.yaml') as fh:
#     struct = yaml.load(fh)
# print(json.dumps(struct, indent=4, separators=(',', ': ')))

# yaml.dump stores a reference to object on disk but not the object class code, therefore the class
# imlementation should stay reachable
class MyClass:
    def __init__(self, init_val):
        self.val = init_val
    def increment(self):
        self.val += 1
cc = MyClass(5)
cc.increment() ; cc.increment()
with open("obj.yaml", 'wb') as fh:
    yaml.dump(cc, fh)
with open("obj.yaml", 'rb') as fh:
    inst = yaml.load(fh)
    inst = yaml.safe_load(fh) # limit the loading of objects to python plain structures (like lists, dicts, tuples etc.)
    # and not instances belongs to our classes (created by us) because an instance can easily 
    #contains malicious code (we need to make sure we is the source before loading)
print("instance is : ",unpickled_cc) ; print("instance attr value is : ",unpickled_cc.val)