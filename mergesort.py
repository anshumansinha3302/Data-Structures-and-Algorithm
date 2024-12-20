# Merge Sort Algorithm
# Merge Sort is a divide and conquer algorithm. It divides the array into two halves, recursively sorts both halves,
# and then merges the two sorted halves into a single sorted array.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left = arr[:mid]  # Divide the array into two halves
        right = arr[mid:]

        merge_sort(left)  # Recursively sort the first half
        merge_sort(right)  # Recursively sort the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Check if any element was left in the left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Check if any element was left in the right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sorted Array:", merge_sort(arr))
