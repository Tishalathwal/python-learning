# Problem: Calculate the sum of even numbers up to a given number n.


number = int(input("Enter a number: "))
even_sum = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        even_sum += i

print("Sum of even numbers:", even_sum)
