#  Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["mango", "banana", "orange", "apple", "grapes"]

for item in items:
    if items.count(item) > 1:
        print("Duplicate found:", item)
        break
else:
    print("All elements are unique.")