# # Return area and parameter of squarer

# def cal(side):
#     parameter= 4*side
#     area= side**2
#     return[parameter, area]

# area=cal(4)[1]
# print(area)
# para= cal(4)[0]
# print(para)

## lambda
# cube= lambda x: x**3
# print(cube(4))

## write a function that takes variable number of arguments and returns their sum

# def sumAll(*args):
#     sum=0
#     for num in args:#args is tuple, like rest operator in js
#         sum+=num
#     return sum

# print(sumAll(1,2,3,4))
# print(sumAll(5,6,7))

## **kwargs-dictionary


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_kwargs(name="Jon", power="strong")
# print_kwargs(power="strong", name="Jon", enemy="Night king")
# print_kwargs(power="strong", location="winterfell")

## generator function with yield
# def even_generator(limit):
#     for i in range(2, limit+1, 2):
#         yield i

# for num in even_generator(10):
#     print(num)

# #### MAX and MIN in Python
# print(2**100>float("inf"))## max
# print(2**500<float("-inf"))## min

#### Initialize lists
# li= [1]*5
# print(li)

a,b,c=[1,3,5]
print(a,b,c)