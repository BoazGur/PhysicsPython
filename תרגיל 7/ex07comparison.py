import time
from numpy import random
import ex07vanilla
import ex07pandas


data = [{ 'A': random.rand() * 100, 'B': random.rand() * 100} for _ in range(1000)]

iterations = 1000
vanilla = 0
pandas = 0
for _ in range(iterations):
    t1 = time.time()
    ex07vanilla.calc(data, 'A', 'B')
    t2 = time.time()

    vanilla += t2 - t1

    t1 = time.time()
    ex07pandas.calc(data, 'A', 'B')
    t2 = time.time()

    pandas += t2 - t1

print(f'Vanilla ran on average {vanilla / iterations} seconds')
print(f'Pandas ran on average {pandas / iterations} seconds')
print(f'Pandas was {pandas / vanilla}x slower')

# Vanilla ran on average 0.0002563800811767578 seconds
# Pandas ran on average 0.0028581881523132326 seconds
# Pandas was 11.148245757605064x slower