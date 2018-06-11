Percentage = int(input("Enter your percentage"))
if Percentage >= 90:
    print("O Grade")
elif 80 <= Percentage < 90:
    print("A Grade")
elif 70 <= Percentage < 80:
    print("B Grade")
elif 60 <= Percentage < 70:
    print("C Grade")
elif 50 <= Percentage < 60:
    print("D Grade")
elif 40 <= Percentage < 50:
    print("E Grade")
else:
    print("Fail")