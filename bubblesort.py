# Bubble Sort Algorithm
# Bubble Sort repeatedly compares adjacent elements in the list and swaps them if they are in the wrong order.
# This process is repeated for every element in the list, which results in the largest element "bubbling up" to the end of the list.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Traverse through all elements in the array
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sorted Array:", bubble_sort(arr))
