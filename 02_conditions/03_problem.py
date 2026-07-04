# problem- 3 assign a letter grade based on a student's score:A(90-100), B(80-89), C(70-79),D(60-69) and F(below 60)

score = 600
if score>=101:
    print("please verify grade")
    exit()

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="E"

    print("grade is", grade)
