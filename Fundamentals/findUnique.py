# arr= [4,1,2,1,2]

# length= len(arr)

# for i in range(length):
#     count=0
#     for j in range(length):
#         if arr[i]==arr[j]:
#             count+=1
#     if(count==1):
#         print(arr[i])
#         break

######################   USING DICTIONARY   ###################

# frequency= {}
# arr= [3,4,4,4,3,1,2,0,2,0,3]

# for element in arr:
#     if element in frequency:
#         frequency[element]+=1
#     else:
#         frequency[element]=1

# for key, value in frequency.items():
#     if value==1:
#         print(key)
#         break

#################   USING XOR(only for even duplicates)   ######################

arr= [3,4,3,2,1,2,4]
ans=0
for element in arr:
    ans= ans^element
print(ans)
