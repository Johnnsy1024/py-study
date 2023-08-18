def heapyify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapyify(arr, n, smallest)
        
def build_min_heap(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1 , -1):
        heapyify(arr, n, i)

arr = [4, 10, 3, 5, 1, 7, 6]
build_min_heap(arr)
print(arr)