#Implement a recursive function to calculate the factorial of a given number.


def factorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)
num = int(input("Enter a value: "))
result = factorial(num)

print("The factorial of {} is {}.".format(num,result))