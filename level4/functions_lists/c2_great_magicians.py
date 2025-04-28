import c1_magicians

print(">"*20)

magicians = c1_magicians.magicians

def make_great(magicians: list[str]):
    for index, magician in enumerate(magicians):
        magicians[index] = magician + " the Great"
    return magicians

magicians = make_great(magicians)

c1_magicians.show_magicians(magicians)