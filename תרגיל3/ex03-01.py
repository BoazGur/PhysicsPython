def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**(1/2) + 1)):
        if num % i == 0:
            return False
        
    return True

## Main

sum_ = 0
num = 1 # Arbitrary positive number
while num > 0:
    num = int(input('Please enter a number: '))

    if is_prime(num):
        sum_ += num

print('Result =', sum_)