# Problem: Given a string, find the first non-repeated character.

str = "teeter"

for char in str:
    if str.count(char) == 1:  # here count means how many times the character is present in the string and 1 indicates that the character is not repeated
        print("First non-repeated character:", char)
        break