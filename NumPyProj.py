import numpy as np

def main():
    # Generate a random array of size 5x5
    random_array = np.random.rand(5, 5)
    print("Random Array:")
    print(random_array)
    print()

    # Calculate the mean of the array
    mean_value = np.mean(random_array)
    print("Mean Value of the Array:", mean_value)
    print()

    # Calculate the sum of each column
    column_sums = np.sum(random_array, axis=0)
    print("Sum of Each Column:")
    print(column_sums)
    print()

    # Calculate the product of each row
    row_products = np.prod(random_array, axis=1)
    print("Product of Each Row:")
    print(row_products)
    print()

if __name__ == "__main__":
    main()

print('ALL DONE Hosein')