import random

def n_average(n):
    sum = 0
    for _ in range(n):
        sum += random.randint(1, 100)
    
    return sum / n

def standard_deviation(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(1, 100))

    avg = sum(nums) / n
    squared = [(num - avg)**2 for num in nums]

    return (sum(squared) / n) ** 0.5