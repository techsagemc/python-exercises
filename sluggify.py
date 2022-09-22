
# def slugify(phrase):
#     return phrase.lower().strip().replace(" ","-")
    

# slugify("Hello WoRld I loVe you         ")

def count_vowels(phrase):
    count = 0
    for char in phrase:
        if char in "aeiou":
            count += 1
    return count

count_vowels("hello world")