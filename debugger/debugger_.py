import pdb

# values = [1, 2, 3, 4, 5 , 6, 7, 8 ,9 , 10]
#
# for val in values:
#     my_sum = 0
#     my_sum = my_sum + val
#     pdb.set_trace()
#
# print(my_sum)

def doubleval(argsum, val):
    argsum = 0
    newval = argsum + val
    return newval
pdb.set_trace()
values = [1, 2, 3, 4, 5 , 6, 7, 8 ,9 , 10]
my_sum = 0

for val in values:
    my_sum = doubleval(my_sum, val)

print(my_sum)