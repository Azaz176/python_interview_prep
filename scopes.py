# x =99
# def f1():
#     x=11
#     def f2():
#         print(x)
#     return f2
# y=f1()
# y()# closure

def jon(num):
    def actual(x):
        return x ** num
    return actual

f= jon(2)
g=jon(3)
print(f(2))
print(g(3))