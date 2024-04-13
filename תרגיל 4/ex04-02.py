import myfuncs

n = int(input('Enter n: '))
epsilon = float(input('Enter epsilon: '))

rounds = 1000
count = 0
for i in range(rounds):
    avg = myfuncs.n_average(n)
    if avg > 50 + epsilon: # I have decided to only look above 50
        count += 1

print(f'Result: {(count / rounds) * 100 : .1f}%')