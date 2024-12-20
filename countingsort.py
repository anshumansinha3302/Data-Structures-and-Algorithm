# Counting Sort Algorithm
# Counting Sort assumes that the input consists of integers in a specific range.
# It counts the number of occurrences of each distinct element and uses this information to place the elements in the correct position.
def counting_sort(arr):
    max_val = max(arr)  # Find the maximum element
    min_val = min(arr)  # Find the minimum element
    range_of_elements = max_val - min_val + 1  # Calculate the range of the elements
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Store cumulative count
    for i in range(1, range_of_elements):
        count[i] += count[i-1]

    # Place the elements in sorted order
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
print("Counting Sorted Array:", counting_sort(arr))
