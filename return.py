# def laugh(strength=2):
#     print("HA" * strength)

# laugh(10)


def sluggify(phrase, sep="-"):
    return phrase.lower().strip().replace(" ",sep )

sluggify("helo world is trash")