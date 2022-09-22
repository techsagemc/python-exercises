
for num in range(99,0,-1):
    if num >= 2:
        print(f"{num} bottles of beer on the wall")
        print(f"{num} bottles of beer.")
    if num == 2:
        print(f"take one down, pass it around, {num - 1} bottle of beer on the wall.")
    
    elif num == 1:
        print(f"{num} bottle of beer on the wall")
        print(f"{num} bottle of beer.")
        print(f"take one down, pass it around, no more bottles of beer on the wall.")
        
    else: 
        print(f"take one down, pass it around, {num - 1} bottles of beer on the wall.")
    
    print("*" * 50)
    
    
