import random

print("What is my magic number (1 to 100) ? ")
mynum = random.randint(1,10)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynum:
    msg = str(ntries) + ">> "
    if (ntries == 6):
        print("you last chance")
    yourguess = int(input(msg))
    if yourguess > mynum:
        print("Too high")
    else:
        print("Too low")
    ntries += 1
if yourguess == mynum:
    print("Yes it is!!", mynum)
else:
    print("Sorry! My num is", mynum)