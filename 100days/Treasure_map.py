# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #23
# 🚨 Don't change the code above 👆

#Write your code below this row horizontal
horizontal = int(position[0]) #2 First number from input 
vertical = int(position[1]) #3 Second number from input

selected_row = map[vertical - 1][horizontal - 1] = "X" #map is the array and I put the indexes on the end to specify location

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

