'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here

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
