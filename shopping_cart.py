print("WELCOME TO OUR USELESS STORE!")
print("*" * 20)
buy = input('What item are you buying?')
price = float(input(f'What is the price of {buy}: '))
amount = float(input(f'How many {buy} are you buying?'))


print(f"Added {amount} {buy} to the cart")
print(f"Subtotal: ${price * amount}")