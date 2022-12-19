t= []
for i in range (1,125):
    if (125%i == 200%i and 125%i == 350%i and 350%i == 200%i ):
        t.append(i)
print(max(t))

print("--------ikinci yöntem----------")
for i in range(1,350):
    if 125 % i == 200 % i and  125 % i == 350 % i and 200 % i == 350 % i:
        a = i
print(a)

