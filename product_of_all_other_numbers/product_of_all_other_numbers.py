'''
Input: a List of integers
Returns: a List of integers
'''

import math


def product_of_all_other_numbers(arr):
    # Your code here
    index = 0
    some_arr = []
    while index < len(arr):
        product = 1

        for i in range(0, len(arr)):
            if index != i:
                product *= arr[i]

        some_arr.append(product)
        index += 1
    arr.clear()
    arr.extend(some_arr)
    return arr
    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    #  [13547520, 10536960, 94832640, 11854080, 15805440, 13547520, 11854080, 11854080, 13547520, 9483264]

    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
