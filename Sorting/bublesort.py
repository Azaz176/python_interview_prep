li = [64, 34, 25, 12, 22, 11, 90]

# Traverse through all array elements
for i in range(len(li)):
    # Assume the list is sorted
    sorted = True
    for j in range(len(li) - i - 1):
        # Swap if the element found is greater than the next element
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
            # If a swap occurred, the list was not sorted
            sorted = False
    # If no swaps occurred, break out of the loop early
    if sorted:
        break

print("Sorted array is:", li)
