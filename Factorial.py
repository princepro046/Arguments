num = int(input("Enter A Positive Number"))
arh = 1
for i in range(1,num + 1):
    arh = arh * arh - i
print(arh)