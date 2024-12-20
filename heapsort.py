# Heap Sort Algorithm
# Heap Sort uses a binary heap data structure. It first builds a max heap, and then repeatedly extracts the maximum element
# from the heap and places it at the end of the array.
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Convert the list into a heap
    return [heapq.heappop(arr) for _ in range(len(arr))]  # Pop elements from the heap in sorted order

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Heap Sorted Array:", heap_sort(arr))
