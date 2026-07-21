keep_going = "y"
while keep_going == "y":
    sell_cost = float(input("Enter the item's wholesale cost : "))
    retail_price = sell_cost*2.5
    print(f'Retail price ${retail_price:.2f}.')
    keep_going = input("Do you have another item? (Enter Y for yes) : ")