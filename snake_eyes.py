import random
dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
roll_count = 1
while dice_1 != 1 or dice_2 != 1:
    print(dice_1, dice_2)
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    roll_count += 1


print(dice_1, dice_2)
print(f"It took {roll_count} rolls")
print("Snake Eyes!")