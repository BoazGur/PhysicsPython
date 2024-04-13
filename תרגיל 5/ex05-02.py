import numpy as np

filename = 'data05-02.txt'

start = 0
end = None
lines = 1
with open(filename) as f:
    for i, line in enumerate(f):
        if 'table 2' in line:
            start = i + 1
        if 'table 3' in line:
            break

        end = i
        lines += 1

table2 = np.genfromtxt(filename, delimiter=',', skip_header=start, skip_footer=lines-end)
print(table2)