def swapFileData(a,b):
    print("The first file is:",a)
    print("The second file is:",b)

data_a = open("s1.txt")
print(data_a.read())
#swapFileData(data_a,data_b)

data_b = open("s2.txt")
print(data_b.read())
#swapFileData(data_b,data_a)

swapFileData(data_a,data_b)