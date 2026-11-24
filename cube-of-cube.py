def cube(number):
    return number*number*number

def check(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

num = int(input("Enter your number: "))

print(check(num))



