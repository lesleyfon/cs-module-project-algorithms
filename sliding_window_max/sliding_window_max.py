'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    '''
        Steps:
            1 - Create a list to hold all the max in a given window.
            2 - Create two variables to keep track of the begining index of a window and the end index of a window. 
            3 - While the end index of a window is less than the length of the length of the nums list. we want to keep looping
            4 - Create a variable to hold the elements in a current window and slice those elements using the start_window_index and end_window_index
            5 - Get the max value in the current_window and add it to the window_max list
            6 - Return the window_max list at the end of the loop
    '''
    window_max = []
    start_window_index = 0
    end_window_index = k - 1
    while end_window_index < len(nums):
        current_window = nums[start_window_index: end_window_index + 1]

        max_value = max(current_window)
        window_max.append(max_value)

        start_window_index += 1
        end_window_index += 1
    return window_max
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
