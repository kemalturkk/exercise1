def tops (n):
    t=0
    for i in str(n):
        t+= int(str(i))
    return t


for i in range(2005):
    if (tops(i)== (2005-i)):
        print(i)
        