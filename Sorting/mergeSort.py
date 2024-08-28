def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Merge the two parts in place
    while start <= mid and start2 <= end:

        # If the element at start is already in place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            # Element at start2 is smaller than element at start
            value = arr[start2]
            index = start2

            # Shift all the elements between start and start2 right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all pointers
            start += 1
            mid += 1
            start2 += 1

def merge_sort_in_place(arr, start, end):
    if start < end:

        # Calculate mid point
        mid = start + (end - start) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, start, mid)
        merge_sort_in_place(arr, mid + 1, end)

        # Merge the sorted halves
        merge_in_place(arr, start, mid, end)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort_in_place(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
