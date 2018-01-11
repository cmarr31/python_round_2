# Write a program that takes a list of strings and a string containing a single character, and 
# prints a new list of all the strings containing that character.

def find_characters(lst, char):
    new_list = []
    for i in lst:
        if char in i:
            new_list.append(i)
    print new_list
find_characters(["hello", "my", "name", "is", "Chris"], "i")