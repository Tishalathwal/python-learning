# Problem: Write a function that takes variable number of arguments and returns their sum.

def num(*args):
    return sum(args)

print("sum is: ",num(1,2,3))
print("sum is: ",num(1,2,3,4,5))
print("sum is: ",num(1,2,3,4,5,6,7,8,9))