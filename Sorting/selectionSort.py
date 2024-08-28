li = [13, 46, 25, 52, 20, 9]

for i in range(len(li)):
    min_index = i
    for j in range(i+1, len(li)):
        if li[j] < li[min_index]:
            min_index = j
    
    # Swap the found minimum element with the first element
    li[i], li[min_index] = li[min_index], li[i]

print(li)
