# Shell Sort Algorithm
# Shell Sort is an optimization of Insertion Sort. It starts with large gaps between elements and progressively reduces the gap.
# This helps elements move to their correct position faster than the standard Insertion Sort.
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        # Perform a gap insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap size
    return arr

arr = [5, 3, 8, 6, 2, 7, 4, 1]
print("Shell Sorted Array:", shell_sort(arr))
