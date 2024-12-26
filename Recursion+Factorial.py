num = int(input("Enter Your Positive Number :"))


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(num))


    
