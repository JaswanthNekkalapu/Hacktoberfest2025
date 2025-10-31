def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
index = binary_search(sorted_list, target_value)
if index != -1:
     print(f"Target found at index: {index}")
else:
     print("Target not found")
