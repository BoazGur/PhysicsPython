a = 15
b = 7
c = 30

if a < b and a < c and b < c:
    print(f'{a}, {b}, {c}')
    print(f'{c}, {b}, {a}')
elif a > b and a < c:
    print(f'{b}, {a}, {c}')
    print(f'{c}, {a}, {b}')
elif a > c and a < b :
    print(f'{c}, {a}, {b}')
    print(f'{b}, {a}, {c}')
elif a > c and a > b and b < c:
    print(f'{b}, {c}, {a}')
    print(f'{a}, {c}, {b}')
elif a > c and a > b and b > c:
    print(f'{c}, {b}, {a}')
    print(f'{a}, {b}, {c}')
else:
    print(f'{a}, {c}, {b}')
    print(f'{b}, {c}, {a}')