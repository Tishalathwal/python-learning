# Problem-2 Movie ticket are priced based on age $12 for adults(18 and over), $8 for children. Everyone get $2 discount on wednesday


age = 5
day ="Wednesday"

price= 12 if age>=18 else 8

if day=="Wednesday":
    price=price-2

print("ticket price for you is $", price)
