li= [1,2,3,4,5,6]

for i in range(0,len(li), 2):
    if(i+1<len(li)):
        li[i], li[i+1]=li[i+1], li[i]
    
print(li)