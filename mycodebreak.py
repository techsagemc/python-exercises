# Lets practice string slices!!
# This is just decoration
print("Welcome to python slices")
print("*" * 20)

# I want whatever the user types in to print out reversed

def word1():
    word1 = input("Pick a random word. ")
    if word1:
        return word1[::-1]

#Execute the defined function
word1()