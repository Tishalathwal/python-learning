#  basics examples of scope

x = 10  # global variable
print(x)  # 10

def my_function():
    y = 20  # local variable
    print(x)  # 10 (global variable)
    print(y)  # 20 (local variable)

my_function()


print(x) 
# print(y)  # NameError: name 'y' is not defined (local variable)


