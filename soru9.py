def basamaklarToplami(n):
    t=0
    for i in (str(n)):
        t+= int(str(i))
    return t
liste = []
for x in range (999):
    if (basamaklarToplami(x)<9):
        print(x,end= " ")
        
        
print("             ---------ikinci yöntem------------")


a = 0
for i in range(1,1000):
    b = 0
    for c in range(len(str(i))):
        b += int(str(i)[c])
    if b < 9:
        print(i,end =  " ")