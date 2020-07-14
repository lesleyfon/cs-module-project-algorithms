'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    heap = []
    index = 0

    while index < len(arr):

        if arr[index] in heap:
            heap.remove(arr[index])
        else:
            heap.append(arr[index])
        index += 1
    return heap[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
