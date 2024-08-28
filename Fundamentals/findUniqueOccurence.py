arr= [1,2,2,1,1,3]
frequency={}
uniqueOccur=set()
for element in arr:
    if element in frequency:
        frequency[element]+=1
    else:
        frequency[element]=1

#print(frequency)
ans=True
for key in frequency:
    if frequency[key] in uniqueOccur:
        ans=False
        break
    else:
        uniqueOccur.add(frequency[key])
print(ans)     