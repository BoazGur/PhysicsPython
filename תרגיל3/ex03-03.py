def lcm(num1, num2, num3):
    bigger = max(num1, num2, num3)

    while True:
        if (bigger % num1 == 0) and (bigger % num2 == 0) and (bigger % num3 == 0):
            return bigger
        
        bigger += 1

## Main
a = int(input('Please enter a: '))
b = int(input('Please enter b: '))
c = int(input('Please enter c: '))
result = lcm(a, b, c)

print('Result =', result)