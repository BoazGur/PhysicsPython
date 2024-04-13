num_of_products = int(input('Please enter number of products: ')) # Get number of products

minimum = float('inf') # Can only go down from here
maximum = 0 # Can only go up from here
average = 0
for i in range(1, num_of_products + 1):
    price = int(input(f'Please enter price of product {i}: '))
    average += price # Add all prices

    if price > maximum: # If new price is bigger than all other prices seen already
        maximum = price
    if price < minimum: # If new price is lower than all other prices seen already
        minimum = price

average /= num_of_products # Calculate average

# Print
print('Highest price is', maximum)
print('Lowest price is', minimum)
print('Average price is', average)