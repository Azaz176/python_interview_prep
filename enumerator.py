#Enumerator- enumerate is a built-in Python function that allows you to loop over a list (or any iterable) and get both the index and the value at the same time.
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# x =("ab", "bc", "cd")
# y= enumerate(x)
# print(y)
# print(list(y))#[(0, 'ab'), (1, 'bc'), (2, 'cd')]

list= [{'name':"Azaz", "Fruit":"mango"}, {"name":"bha", "fruit":"anar"}]
# print(list)
for i in enumerate(list, start=1):#indexing starts from 1 of tuple
    print(i)
for index, content in enumerate(list, start=1):
    print(f"{index}->{content['name']}")