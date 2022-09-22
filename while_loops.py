num = int(input("Guess a number between 1 and 10"))
guess = 3

while num != 2:
    print("Wrong answer!!")
    guess -= 1
    num = int(input("Guess again.."))
    if guess == 1:
        print("too many attemps...please try again later")
        exit()
    
else:
    print("Correct!!")