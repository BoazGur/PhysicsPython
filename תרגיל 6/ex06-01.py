while True:
    nums_input = input('Please enter five numbers: ')
    nums = nums_input.split(',')

    # check if valid number of numbers
    if len(nums) != 5:
        print('Error.', end=' ')
        continue

    # check if can be interpreted as numbers
    try:
        nums = [float(num) for num in nums]
    except:
        print('Error.', end=' ')
        continue

    # passed all checks, can get out of loop
    break

print(f'Result: {(max(nums) + min(nums)) / 2}')