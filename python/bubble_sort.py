def bubble_sort(arr):
    """
    Bubble Sort algorithm: sorts arr in ascending order
    Time Complexity: O(n^2) in worst case
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted:", sorted_arr)
