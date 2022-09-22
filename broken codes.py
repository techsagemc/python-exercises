# Hi Michael, 

# I've been reading a bit about the "for loop" 
# Here is my broken code for you to fix :)

# # Ask the user to input his name and how many times should python greet him/her.
# print("What is your name? ")
# name = input()
# print("Hello", name, "!")
# print("How many times do you want me to say 'hello' ?")
# x = input()
# for i in range (x):
#     print("hello")

# Enjoy 



# My answer
# I used the question as a placeholder in the input function
name = input("What is your name?")

# I used the f string to be able to add information from variables into the print function
print(f"Hello {name}!")
# I used the question as a placeholder in the input function again
# The input would most likely be a number so i converted the input from a string to an integer
x = int(input("How many times do you want me to say hello?"))

#I want hello to print as many times as the input the user puts in
for greeting in range(x):
    print("hello")
