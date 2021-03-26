import random

running = True
while running:
    diceOne = random.randint(0, 6)
    diceTwo = random.randint(0, 6)
    if diceOne + diceTwo == 7:
        print(f'We got 7 from {diceOne} and {diceTwo}')
        running = False
    else:
        print(f'Roll : {diceOne} and {diceTwo}')
input()