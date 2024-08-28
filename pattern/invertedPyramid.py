n = int(input("number"))

for i in range(n):
    for space in range(i):
        print(" ", end=" ")
    
    for j in range(n - i):
        print("*", end=" ")
    
    for star in range(n - i - 1):
        print("*", end=" ")
    
    print()
