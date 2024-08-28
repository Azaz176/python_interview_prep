n = int(input("number"))

for i in range(n):
    for space in range(n - i - 1):
        print(" ", end=" ")
    
    for j in range(i + 1):
        print("*", end=" ")
    
    for star in range(i):
        print("*", end=" ")

    print()
