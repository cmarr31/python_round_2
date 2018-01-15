name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "monkeys"]

def make_dict(list1, list2):
    if (len(list1) >= len(list2)):
        new_dict = dict(zip(list1, list2))
        print new_dict
    else:
        new_dict = dict(zip(list2, list1))
        print new_dict
    return new_dict
make_dict(name, favorite_animal)