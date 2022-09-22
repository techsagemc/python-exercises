from random import randint

dice_number = int(input("How many dice are we rolling?"))
dice_sides = int(input("How many sides on each die?"))

randint(1,dice_sides)

while True:
    for die in range(dice_number):
        print(randint(1,dice_sides))
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        break
    
    
 
    

