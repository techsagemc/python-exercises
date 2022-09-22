first_name = input("What is your first name?")
last_name = input("What is you last name?")
whole_name = len(first_name) + len(last_name)

if whole_name < 12:
    print("Your name is shorter than the average American name")

elif whole_name == 12:
    print("Your name is the average length of an American name")
    
else:
    print("Your name is longer than the average American name")


