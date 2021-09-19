from solution_1task import FileReader
reader = FileReader("C:\\Users\\vikto\Desktop\\file_class1.txt")
text = reader.read()
print(text)
with open("C:\\Users\\vikto\Desktop\\file_class2.txt", "w") as file:
    file.write('some text')


reader = FileReader("C:\\Users\\vikto\Desktop\\file_class2.txt")
text = reader.read()
print(text)
print(type(reader))