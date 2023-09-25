day = int(input("day: "))
if day == 1:
    print("mondey")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day ==6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("day of week")

#task 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 == num2:
    print("Equal numbers")
elif num1 < num2:
    print(num1, num2)
elif num1 > num2:
    print(num2, num1)
else:
    print("resault: ")

#task3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n1.+\n2.-\n3.* \n4. /")
option = int(input("option: "))
if option == 1:
    print(num1 + num2 )
elif option == 2:
    print(num1 - num2)
elif option == 3:
    print(num1 * num2)
elif option == 4:
    print(num1 / num2)
else:
    print("resault")


