fn quick_sort(arr: &mut [i32]) {
    if arr.len() <= 1 {
        return; // Base case: arrays with 0 or 1 element are already sorted
    }

    let pivot_index = partition(arr);
    quick_sort(&mut arr[0..pivot_index]); // Recursively sort the left part
    quick_sort(&mut arr[pivot_index + 1..]); // Recursively sort the right part
}

fn partition(arr: &mut [i32]) -> usize {
    let pivot = arr[arr.len() - 1]; // Choose the last element as the pivot
    let mut i = 0; // Pointer for the smaller element

    for j in 0..arr.len() - 1 {
        if arr[j] <= pivot {
            arr.swap(i, j); // Swap if the current element is smaller than or equal to the pivot
            i += 1; // Move the pointer for the smaller element
        }
    }
    arr.swap(i, arr.len() - 1); // Place the pivot in the correct position
    i // Return the index of the pivot
}

fn main() {
    let mut arr = [10, 7, 8, 9, 1, 5];
    println!("Original array: {:?}", arr);
    quick_sort(&mut arr);
    println!("Sorted array: {:?}", arr);
}
