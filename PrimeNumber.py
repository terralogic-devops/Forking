number = int(input("Enter a number"))
count = 0
for i in range(2,int(number/2)):
    if number % i == 0:
        print("Not Prime")
        count = +1
        break
if count == 0:
    print("Prime")