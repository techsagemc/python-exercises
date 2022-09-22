tweet = input("Enter your tweet: ")
char_length = len(tweet)
over_max = char_length - 145

print("x" * 50)
if char_length <= 145:
    print(f"Your {char_length} char tweet will work!")
elif char_length == 146:
    print(f"Your {char_length} char tweet is {over_max} char too long!")
else:
    print(f"Your {char_length} char tweet is {over_max} chars too long!")

print("x" * 50)