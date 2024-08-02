import time

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = mergesort(left_half)
    right_half = mergesort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged += left[i:]
    merged += right[j:]
    
    return merged

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

start = time.time()
sorted_arr = mergesort(arr)
end = time.time()

print("Sorted array is:", sorted_arr)
print("time taken:", end-start)