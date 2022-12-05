# class MyDict(dict):
#     def __setitem__(self, key, val):
#         print("setting a key and value!")
#         dict.__setitem__(self,key,val)
#
# dd = MyDict()
# dd['a'] = 5
# dd['b'] = 6
# for key in dd.keys():
#     print('{0}={1}'.format(key,dd[key]))
#
# class MyList(list):
#
#     def __getitem__(self, index):
#         if index == 0: raise IndexError
#         if index > 0: index -=1
#         return list.__getitem__(self,index)
#
#     def  __setitem__(self, index, value):
#         if index == 0: raise IndexError
#         if index > 0: index -=1
#         return list.__setitem__(self, index, value)
# x = MyList([1, 2, 3, 4])
# print(x)
# x.append(5)
# print(x[1])
# print(x[5])

class GetSet:
    __mangled_name = "I live just in this class"
    def __init__(self, value):
        self._attrval = value
    @property
    def var(self):
        print ("getting the \"var\" attribute")
        return self.attrval
    @var.setter
    def var(self,val):
        print("setting the \"var\" attribute")
        self.attrval = val
    @var.deleter
    def var(self):
        print("deleting the \"var\" attribute")
        self.attrval = None

me = GetSet(5)
# me.var = 1000
# print(me.var)
# del me.var
# print(me.var)
# print(me._attrval)
print(me._GetSet__mangled_name)
