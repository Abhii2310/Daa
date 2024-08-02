import time 
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Input values directly
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))




start = time.time()
sorted_arr = quicksort(arr)
end = time.time()

print("Sorted array is:", sorted_arr)
print("time taken:", end-start)