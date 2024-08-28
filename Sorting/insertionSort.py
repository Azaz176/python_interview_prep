li = [13, 46, 25, 52, 20, 9]

for i in range(1, len(li)):
    key = li[i]
    j = i - 1
    
    # Move elements of li[0..i-1] that are greater than key
    # to one position ahead of their current position
    while j >= 0 and key < li[j]:
        li[j + 1] = li[j]
        j -= 1
    li[j + 1] = key

print(li)
