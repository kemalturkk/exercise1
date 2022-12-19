k = 0
for i in range(1000,10000):
    if int(str(i)[0]) > int(str(i)[3]):
        k += 1
        
print(k)
