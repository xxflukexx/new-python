col = int(input("Enter number of col : "))
for i in range(1,101):
    print(i,"\t",end = "")
    if i%col==0:
        print()