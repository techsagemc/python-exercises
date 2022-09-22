# Create an interactive, text-based todo list that has the following features:

# - A user can add todos by entering them into the prompt
# - A user can complete todos by entering the todo’s corresponding number
# - A user can view a help screen by typing ‘h’ or ‘help’
# - A user can quit by typing ‘q’ or ‘quit

# When a user first runs the script, there are no todos in the list.  They can add one by simply entering it into the prompt as seen below (user input is in green)

#   _____         _           
#  |_   _|__   __| | ___  ___ 
#    | |/ _ \ / _` |/ _ \/ __|
#    | | (_) | (_| | (_) \__ \
#    |_|\___/ \__,_|\___/|___/
                            

# ***********************************
# Enter a command. Type 'h' for help: 
# > walk dog
# 1) walk dog
# ***********************************
# Enter a command. Type 'h' for help: 
# > wash dog
# 1) walk dog
# 2) wash dog
# ***********************************
# Enter a command. Type 'h' for help: 
# > edit video 
# 1) walk dog
# 2) wash dog
# 3) edit video
# ***********************************
# Enter a command. Type 'h' for help: 
# >

# As you can see, each todo in the list is displayed to the user along with a corresponding number.  A user can enter that number to complete a specific todo:

# 1) walk dog
# 2) wash dog
# 3) edit video
# ***********************************
# Enter a command. Type 'h' for help: 
# > 2
# 1) walk dog
# 2) edit video
# **********************************

# A user can type ‘h’ or ‘help’ to view a help menu:

# ```
# Enter a command. Type 'h' for help: 
# > **h**
# TODO LIST HELP
# Type 'q' to quit
# To add a todo to the list, type it and hit enter
# To complete a todo enter its number
# ```

# A user can type ‘q’ or ‘quit’ to quit the app.  The script should display any completed todos in a summary after a user quits:

# Enter a command. Type 'h' for help: 
# > q
# Today you completed 5 todos: 
# * wash dog
# * walk dog
# * walk fish
# * edit video
# * cook dinner

header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos = []
completed = []
# Keep adding to your to do list until you're done
while True:
    # print out the number position of the to do item and the to do item itself
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
        
    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    # ask user for input for the todo list
    command = input("> ")
    # How to shut down ehn doen or completed
    if command == "q":
        break
    # bring up help menu with list of options
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
        # convert number input by user into integer from index of variable
    elif command.isnumeric():
        idx = int(command) - 1
        # prevent user from inputting a value that doesnt exist
        if idx >= len(todos):
            print("THERE IS NO TODO WITH THAT NUMBER!")
        # remove completed tasks from one variable and add to different variable that holds removed variables only
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    # add items to todo list
    else: 
        todos.append(command)
    # Print todos from list
if completed:
    print(f"You completed {len(completed)} todos today: ")
    for todo in completed:
        print(f"* {todo}")

    print("Tasks left undone")
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")

