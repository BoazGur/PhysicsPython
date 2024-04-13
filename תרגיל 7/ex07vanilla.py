def calc(data, key1, key2):
    key1_avg = average(data, key1)

    # loop every column in data
    maximum = -float('inf')
    for col in data:
        if col[key1] > key1_avg and col[key2] > maximum:
            maximum = col[key2]

    return maximum

def average(data, key):
    _sum = 0
    for col in data:
        _sum += col[key]

    return _sum / len(data)


if __name__ == '__main__':
    data = [{ 'A': 20, 'B': 30.5}, { 'A': 15, 'B': 140}, { 'A': 24, 'B': 26.25}]
    print(calc(data, 'A', 'B'))