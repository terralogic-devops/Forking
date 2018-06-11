ls = []
print(type(ls))
max_number = 0
number = int(input("Enter an integer : "))
for i in range(number):
    data = int(input("Enter Number : "))
    ls.append(data)
    if max_number < data:
        max_number = data
print("Maximum number in the given list is :", max_number)