with open("data.txt") as file:
    data = file.read()
    file.seek(0)
    data1 = file.readline()
    file.seek(0)
    data2 = file.readlines()

print(data)
print(data1)
print(data2)