# Quick Sort Algorithm
# Quick Sort is a divide-and-conquer algorithm. It selects a 'pivot' element and partitions the array into two sub-arrays:
# one with elements less than the pivot and the other with elements greater than the pivot. The sub-arrays are then sorted recursively.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Select a pivot element (middle element)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print("Quick Sorted Array:", quick_sort(arr))
