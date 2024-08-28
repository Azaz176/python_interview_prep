def partitioning(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    
    # Index of the smaller element
    i = low - 1
    
    # Traverse through all elements
    # Rearrange elements based on pivot comparison
    for j in range(low, high):
        if arr[j] < pivot:
            # If the current element is smaller than the pivot
            # increment the index of the smaller element and swap
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the partitioning index
    return i + 1

def quick_sort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the partitioning index
        partitionIndex = partitioning(arr, low, high)
        
        # Recursively apply the same logic to the left and right subarrays
        quick_sort_in_place(arr, low, partitionIndex - 1)
        quick_sort_in_place(arr, partitionIndex + 1, high)

# Example usage:
arr = [13, 46, 25, 52, 20, 9]
# Call quick sort on the entire array
quick_sort_in_place(arr, 0, len(arr) - 1)

# Print the sorted array
print(arr)
