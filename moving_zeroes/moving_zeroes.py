'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    '''
        Naive Solution:
            1 create a store to hold none 0 ints and 0 digits
            2. loop though it and remove every element from the array and add to their respective arrays
            3. Concat the zero array to the none zero array. 
            5. Concat every thing in the none_zero array into the arr and return it 
    '''
    zero_store = []
    none_zero = []
    while len(arr) > 0:
        if arr[0] == 0:
            zero_store.append(arr.pop(0))
        else:
            none_zero.append(arr.pop(0))
    pass
    none_zero.extend(zero_store)
    arr.extend(none_zero)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
