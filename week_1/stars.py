x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(lst):
    for item in lst:
        if (type(item) is int):
            print "*" * item
        else:
            print item[:1].lower() * len(item)
draw_stars(x)


y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(y)