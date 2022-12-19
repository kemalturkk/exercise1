t = 0
for i in range(100,1000,2):
    if int(str(i)[0]) == int(str(i)[1]) or int(str(i)[0]) == int(str(i)[2]) or int(str(i)[1]) == int(str(i)[2]):
        t += 1
print(t)

