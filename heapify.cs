using System;

class HeapSort
{
    // Function to perform heapify on a subtree rooted with node i
    void Heapify(int[] arr, int n, int i)
    {
        int largest = i; // Initialize largest as root
        int left = 2 * i + 1; // left = 2*i + 1
        int right = 2 * i + 2; // right = 2*i + 2

        // If left child is larger than root
        if (left < n && arr[left] > arr[largest])
        {
            largest = left;
        }

        // If right child is larger than largest so far
        if (right < n && arr[right] > arr[largest])
        {
            largest = right;
        }

        // If largest is not root
        if (largest != i)
        {
            Swap(arr, i, largest); // Swap root with largest

            // Recursively heapify the affected subtree
            Heapify(arr, n, largest);
        }
    }

    // Function to perform heap sort
    public void Sort(int[] arr)
    {
        int n = arr.Length;

        // Build a maxheap
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            Heapify(arr, n, i);
        }

        // One by one extract elements from heap
        for (int i = n - 1; i >= 0; i--)
        {
            Swap(arr, 0, i); // Move current root to end
            Heapify(arr, i, 0); // Call heapify on the reduced heap
        }
    }

    // Function to swap two elements in the array
    void Swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Function to print the array
    public void PrintArray(int[] arr)
    {
        foreach (var item in arr)
        {
            Console.Write(item + " ");
        }
        Console.WriteLine();
    }

    // Main method to test the heap sort implementation
    public static void Main(string[] args)
    {
        HeapSort heapSort = new HeapSort();
        int[] arr = { 12, 11, 13, 5, 6, 7 };

        Console.WriteLine("Original array:");
        heapSort.PrintArray(arr);

        heapSort.Sort(arr);

        Console.WriteLine("Sorted array:");
        heapSort.PrintArray(arr);
    }
}
