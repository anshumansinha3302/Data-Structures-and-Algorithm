# Bucket Sort Algorithm
# Bucket Sort divides the input into several "buckets," sorts each bucket individually (often using another sorting algorithm),
# and then concatenates all the sorted buckets together to produce the final sorted list.
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)  # Find the minimum and maximum value
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Put elements into their respective buckets
    for i in arr:
        index = (i - min_val) * (bucket_count - 1) // (max_val - min_val)
        buckets[index].append(i)

    # Sort each bucket and concatenate the results
    for i in range(bucket_count):
        buckets[i].sort()

    return [i for bucket in buckets for i in bucket]

arr = [0.42, 0.32, 0.23, 0.52, 0.67, 0.43]
print("Bucket Sorted Array:", bucket_sort(arr))
