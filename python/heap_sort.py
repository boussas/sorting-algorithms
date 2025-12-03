import heapq
def heap_sort(arr):
    heapq.heapify(arr)  
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)
