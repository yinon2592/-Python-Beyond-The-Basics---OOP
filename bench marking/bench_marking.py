import timeit

print("by index :   ", timeit.timeit(stmt="mydict['c']", setup="mydict={'a': 5, 'b': 6, 'c': 7}", number=1000000))
print("by get :   ", timeit.timeit(stmt="mydict.get('c')", setup="mydict={'a': 5, 'b': 6, 'c': 7}", number=1000000))


def testme(this_dict, key):
    return this_dict[key]

# print(timeit.timeit("test_me(mydict, key)", setup="from __main__ import testme; mydict={'a': 1, 'b': 2, 'c': 3}; key='c', number=1000000"))

