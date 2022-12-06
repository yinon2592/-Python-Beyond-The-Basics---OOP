from io import StringIO , SEEK_END
message = "hello"
f = StringIO(initial_value=message, newline= "\n")
f.seek(0,SEEK_END)
print(f.tell())
f.write(" world")
f.writelines('-'.join(["\nmy", "name", "is", "Yinon"]))
print(f.getvalue())

# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(",.qsw")
# print(x,"aaa")
# txt = "     banana     "
# x = txt.rstrip()
# print(x)
# print("of all fruits", x, "is my favorite")

# with open('filename.txt') as fh:
#     for line in fh:
#         line = line.rstrip()
#         print(line)
# fh = open('filename.txt')
# for line in fh:
#     line = line.rstrip()
#     print(line)
# fh.close()