n = int(input('Please enter a natural number n: '))
m = int(input('Please enter a natural number m: '))

for i in range(m):
    if n == 1:      # Reached 1 => finished
        break
    if n % 2 == 0:  # Even
        n //= 2
    else:           # Odd
        n = 3*n + 1

if n == 1:
    print('n reached 1')
else:
    print('n did not reach 1 yet')