t = 0
for i in range(100,1000):
    if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]):
        print(i)
        t += 1
print(f'{t} adettir')
