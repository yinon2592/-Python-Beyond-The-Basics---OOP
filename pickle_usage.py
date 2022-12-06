# import pickle
import pickle


# my_list = ['a', 'b', 'c', 'd']

# store object on disk
# with open("data_file.txt", 'wb') as fh:
#     pickle.dump(my_list, fh)

# retrieve object from disk
# with open("data_file.txt", 'rb') as fh:
#     unpicklelist = pickle.load(fh)
#
# print (unpicklelist ," from type " ,type(unpicklelist))
# my_list_2 = ["a", 2.2, 3, "b"]
# x = pickle.dumps(my_list_2 )
# print (x ," from type " ,type(x)) ; print("\n\n")
# y = pickle.loads(x)
# print (y ," from type " ,type(y))

# this_int =555
# this_string = 'oh my goodness'
# my_dict_of_lists = {
#     'a': [1, 2, 3],
#     'b': [4, 5, 6]
# }
# query_results = [('joe', 22, 'clerk'),('pete', 34, 'salesman')]
#
# with open("data_file.txt", 'wb') as fh:
#     pickle.dump((this_int, this_string, my_dict_of_lists, query_results), fh)
# with open("data_file.txt", 'rb') as fh:
#     tup = pickle.load(fh)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])

class MyClass:
    def __init__(self, init_val):
        self.val = init_val
    def increment(self):
        self.val += 1
cc = MyClass(5)
cc.increment() ; cc.increment()
with open("data_file.txt", 'wb') as fh:
    pickle.dump(cc, fh)
with open("data_file.txt", 'rb') as fh:
    unpickled_cc = pickle.load(fh)
print("instance is : ",unpickled_cc) ; print("instance attr value is : ",unpickled_cc.val)