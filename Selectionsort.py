# Selection Sort Algorithm
# The algorithm divides the list into two parts: sorted and unsorted. It repeatedly selects the smallest element from the unsorted part
# and swaps it with the leftmost unsorted element, thus extending the sorted part of the list.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print("Selection Sorted Array:", selection_sort(arr))
