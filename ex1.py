print('''Please select operations -
1. Add
2. Substract
3. Multiply
4. Divide ''')
option = str(input("Select operations from 1, 2, 3, 4 : "))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if option == '1':
    print(f"{num1}+{num2} = {num1+num2}")
elif option == '2':
    print(f"{num1}-{num2} = {num1-num2}")
elif option == '3':
    print(f"{num1}x{num2} = {num1*num2}")
elif option == '4':
    print(f"{num1}/{num2} = {num1/num2}")

