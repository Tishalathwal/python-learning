#  problem-4 determine if a fruit is ripe, overripe or unripe based on its color(eg banana:green-unripe, yellow-ripe, brown-overripe)


fruit  = "banana"
color="yellow"

if fruit == "banana":
    if color=="green":
        print("unripe")
    elif color=="yellow":
        print("ripe")
    elif color=="brown":
        print("overripe")
    else:
        print("invalid color")