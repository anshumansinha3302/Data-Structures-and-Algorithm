# Radix Sort Algorithm
# Radix Sort works by sorting the elements digit by digit, starting from the least significant digit.
# It uses a stable counting sort for each digit.
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Assuming base 10 numbers

    # Count occurrences of the digits
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in output array in sorted order based on current digit
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Copy the sorted array back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)  # Find the maximum number to determine the number of digits
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)  # Perform counting sort based on each digit
        exp *= 10
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sorted Array:", radix_sort(arr))
