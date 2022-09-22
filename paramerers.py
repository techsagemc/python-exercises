# def greet(msg, person):
#     print(f"{msg}, {person}!")

# greet("hello","mike")

def get_total(price, qty=1, tax=.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))

get_total(150, 2)