def lcm(num1, num2):
    bigger = max(num1, num2)

    while True:
        if (bigger % num1 == 0) and (bigger % num2 == 0):
            return bigger
        
        bigger += 1

## Main
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
result = lcm(num1, num2)

print('Result =', result)