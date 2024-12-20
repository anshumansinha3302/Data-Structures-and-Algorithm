# Insertion Sort Algorithm
# Insertion Sort builds the final sorted array one element at a time. It assumes that the left portion of the array is sorted,
# and it places the current element in the correct position in the sorted portion.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print("Insertion Sorted Array:", insertion_sort(arr))
