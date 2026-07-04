#  Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name ="Tisha"):
    return name

print(f"Hello, {greet()}!")
print(f"Hello, {greet('Alice')}!")
