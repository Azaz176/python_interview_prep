# li= [1, -1, 2, 3, -3, 4, -4, 5]
# positive=0
# for x in li:
#     if(x>0):
#         positive+=1
        
# print(positive)
    
# givenNumber=5
# sum=0
# for i in range(1, givenNumber+1):
#     if(i%2==0):
#         sum=sum+i

# print(sum)


# n=5
# for i in range(1, 11):
#     if(i==5):
#         continue
#     else:
#         print(n,"x", i, n*i)

# # reverse the string
# str= "abcd"
# str2=""
# for char in str:
#     str2=char+str2
# print(str2)
# len=len(str)
# for i in range(0, len):
#     j=len-1-i
#     str2+=str[j]
# print(str2)
# print(str[::-1])


# find first non repeated character
#str="aangbbccabhxghayb"

# for char in str:
#     if (str.count(char)==1):
#         print(char)
#         break

# char_count={}
# for char in str:
#     if char in char_count:
#         char_count[char]+=1
#     else:
#         char_count[char]=1

# for char in str:
#     if(char_count[char]==1):
#         print(char)
#         break

## factorial using while loop

# n=6
# x=1
# while (n>0):
#     x=n*x
#     n=n-1
# print(x)

## input validation: keep asking user for inpute until they enter a number between 1 to 10

# while(True):
#     n= int(input("Enter a number between 1 to 10:"))
#     if 1 <= n <= 10:
#         print("valid number")
#         break
#     else:
#         print("provide the valid number")

## check for prime

# n=5
# isPrime= False
# for i in range(2, n):
#     if(n%i==0):
#         print("non prime")
#         break
#     else:
#         print("prime")
#         break

# import math
# n = 8
# sq = int(math.sqrt(n))#float

# for i in range(2, sq + 1):
#     if n % i == 0:
#         print("non prime")
#         break
# else:
#     print("prime")

## check the unique element in a list, if duplicate then exit and print the duplicate

# li=["a", "b", "c", "a", "x", "b" ]
# unique_item= set()
# for item in li:
#     if(item in unique_item):
#         print("duplicate", item)
#         break
#     else:
#         unique_item.add(item)


## Exponentioal backoff strategy
# import time
# wait_time=1
# max_retries=5
# attempts=0
# while(attempts<max_retries):
#     print("Attemps", attempts+1, "wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1

# def example_function(*args):
#     args_gen = (str(arg) for arg in args)#generator function->converths to string
#     for arg_str in args_gen:
#         print(arg_str)
#         #print(arg_str*5)

# example_function(1,2,3,4)

##
# def func1(*args, **kwargs):
#      print(args)
#      print(str(args))
#      print(kwargs.items())
#      args_value = ', '.join(str(arg) for arg in args)
#      kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
#      print(f" args {args_value} and kwargs {kwargs_value}")
    

# func1( "hjgldj","hello", name="Azaz")
    
## NOTE- 6. Difference from List Comprehension
# The main difference between a generator expression and a list comprehension is that a generator does not create the entire list in memory at once. Instead, it produces each item only when needed.

# List Comprehension: [str(arg) for arg in args] — Creates a complete list immediately.
# Generator Expression: (str(arg) for arg in args) — Produces items one at a time, as needed.

## LIst comprehension
# squares = [x**2 for x in range(1, 6)]
# print(squares)
# even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)
# words = ["apple", "banana", "cherry"]
# word_lengths = [len(word) for word in words]
# print(word_lengths)
# words = ["apple", "banana", "cherry"]
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)



# #################genrator comprehension
# squares = (x**2 for x in range(1, 6))
# for num in squares:
#      print(num)
# squares1= [x**2 for x in range(1, 6)]
# print(squares1)

# for i in range(5, 2, -1):#-1 for decrement of i
#      print(i)




