def swapFile():
    with open("s1.txt","r") as f:
       data_a = f.read()
    with open("s2.txt","w") as d:
       data_b = d.write(data_a)
    with open("s2.txt","r") as c:
        data_c = c.read()
    with open("s1.txt","w") as g:
        data_d = g.write(data_c)

swapFile()