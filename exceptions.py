# import sys
#
# my_dict = {'a':1, 'b':2,'c':3,'d':4,}
# key = input("please input a key: ")
# try:
#     print("testing for error")
#     print (f'the value for {key} is {my_dict[key]}')
# except (KeyErrorm, IndexError):
#     print("trapped error")
#     print("the key " + key +" doesn't exist")
#     sys.exit()
#
# print("program continue")
# def make_delim_line(list_to_join, delim):
#     try:
#         formatted_line = delim.join(list_to_join)
#     except TypeError:
#         raise TypeError("make_delim_line(): arg 1 must be a list or tuple")
#     return formatted_line
# # print(" , ".join(["1","2","3"]))
# # print(make_delim_line(["11","22","33"], " , "))
# make_delim_line(100, " , ")

# try:
#     5/0
# except ZeroDivisionError as e:
#     print(e)
#     print(e.args)
# from re import search
#
# def process_date(this_date):
#     if not search(r'^\d\d\d\d-\d\d-\d\d$',this_date):
#         raise ValueError("please submit date in YYYY-MM-DD format")
#     print(f'the submitted date is {this_date}')
# process_date("1980-01-03")
# print("\n\n")
# process_date("1-3-1980")

class MyError(Exception):
    # called when instance is created
    def __init__(self, *args):
        print("calling init")
        if args:
            self.message = args[0]
        else:
            self.message = ""
    # called when exception instance is raise
    def __str__(self):
        print("calling str")
        if self.message :
            return print(f"here's MYError exception with a message: {self.message}")
        else:
            return print(f"here's MYError exception!")
raise MyError
raise MyError()

raise MyError("Houston, we got a problem")
