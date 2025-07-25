function selectionSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        let min_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        // Swap
        [arr[i], arr[min_idx]] = [arr[min_idx], arr[i]];
    }
    return arr;
}

// Example usage
let arr = [64, 25, 12, 22, 11];
console.log("Original:", arr);
let sortedArr = selectionSort(arr);
console.log("Sorted:", sortedArr);
