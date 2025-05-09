import random
import package

b = int(input("what do you choose ? type 0 for rock, 1 for papper, 2 for scissor."))
print(f'you chose:{package.hands[b]}')

a = random.randint(0,2)
print(f'computer chose:{package.hands[a]}')
if b == a:
    print("it is draw!")
else:
    if b == 0:
        if a == 1:
            print("you are loser!")
        else:
            print("you are winner!")
    elif b == 1:
        if a == 0:
            print("you are winner?")
        else:
            print("you are loser!")
    else:
        if a == 0:
            print("you are loser!")
        else:
            print("you are winner?")
