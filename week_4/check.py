from solution import *
path = "some_file"
file_obj1 = File(path + "_3")
file_obj2 = File(path + "_4")
file_obj1.write("line1\nline2\nline3\n")
file_obj2.write("line4\nline5\nline6\n")
new_file_obj = file_obj1 + file_obj2
print(new_file_obj)
print(new_file_obj.read())
[print(ascii(i)) for i in new_file_obj]
