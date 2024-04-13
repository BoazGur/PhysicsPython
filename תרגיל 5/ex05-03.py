import numpy as np
from time import time

def multiply(mat1, mat2):
    res = np.zeros((mat1.shape[0], mat2.shape[1]))

    for i in range(mat1.shape[0]):
        for j in range(mat2.shape[1]):
            for k in range(mat2.shape[0]):
                res[i][j] += mat1[i][k] * mat2[k][j]
    
    return res

num_metrices = 1000
total_time_multiply = 0
total_time_np_multiply = 0
for _ in range(num_metrices):
    mat1 = np.random.randint(0, 100, (50, 100)) # Matrix 50x100
    mat2 = np.random.randint(0, 100, (100, 30)) # Matrix 100x30

    t1 = time()
    multiply(mat1, mat2)
    t2 = time()

    total_time_multiply += t2 - t1

    t1 = time()
    mat1 @ mat2
    t2 = time()

    total_time_np_multiply += t2 - t1


print(f'The average time for mutiplying with loops 50x100 matrix and 100x30 is: {total_time_multiply/num_metrices}sec')
print(f'The average time for mutiplying with numpy 50x100 matrix and 100x30 is: {total_time_np_multiply/num_metrices}sec')
print(f'Numpy is faster than using python loops by {total_time_multiply/total_time_np_multiply}')

# The average time for mutiplying with loops 50x100 matrix and 100x30 is: 0.13304314136505127sec
# The average time for mutiplying with numpy 50x100 matrix and 100x30 is: 0.0001339864730834961sec
# Numpy is faster than using python loops by 992.9595003380904