num = int(input("Enter the number: "))
temp=num
count = 0
# count the number of digits
while temp != 0:
    count += 1
    temp = temp // 10  

print("Number of digits:", count)


# Reverse the Number
ans = 0
while num != 0:
    rem = num % 10
    ans = ans * 10 + rem  # Shift ans to the left and add the current digit
    num = num // 10

print("Reversed Number:", ans)
