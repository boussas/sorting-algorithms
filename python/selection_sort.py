def selection_sort(arr):
    """
    Selection Sort algorithm: sorts arr in ascending order
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original:", arr)
sorted_arr = selection_sort(arr)
print("Sorted:", sorted_arr)

