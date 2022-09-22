
for num in range(99,0,-1):
    if num != 1:
        print(f"{num} bottles of beer on the wall")
        print(f"{num} bottles of beer.")
        print(f"take one down, pass it around, {num - 1} bottles of beer on the wall.")
    
    else:
        print(f"{num} bottle of beer on the wall")
        print(f"{num} bottle of beer.")
        print("take one down, pass it around, no more bottles of beer on the wall.")
    
    print("*" * 50)
    
    
 