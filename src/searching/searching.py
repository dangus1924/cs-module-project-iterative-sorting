arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    # raise ValueError(f"{target} is not found in the array")


    return -1   # not found
# print(linear_search(arr1,50))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    if not arr:
        return "value not found"
    mid_i = len(arr)//2
    mid_val = arr[mid_i]

    if target == mid_val:
        return mid_i
    if mid_val > target:
        left_half = arr[:mid_i]
        return binary_search(left_half, target)
    if mid_val < target:
        right_half = arr[mid_i+1:]
        result = binary_search(right_half, target)
        if result == "value not found":
            return result
        else: 
            return result + mid_i + 1    


    return -1  # not found
# print(binary_search(arr1, 5))