keep_going = "y"
while keep_going == "y":
    sale = float(input("Enter the amouth of sales : "))
    comm_rate = float(input("Enter the comission rate : "))
    comission = sale*comm_rate
    print(f'the comission is ${comission:.2f}')
    keep_going = input("Do you wanna calulate another comission? (Enter Y for yes)")