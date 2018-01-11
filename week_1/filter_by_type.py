#Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#
#Integer
#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, 
#print "That's a small number"
#
#String
#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 
#characters print "Short sentence."
#
#List
#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values 
#print "Short list."

def test_for_type(val):
    if (type(val) is int):
        if (val >= 100):
            print "That's a big number!"
        else:
            print "That's a small number."
    elif (type(val) is str):
        if (len(val) >= 50):
            print "Long sentence."
        else:
            print "Short sentence."
    elif (type(val) is list):
        if (len(val) >= 10):
            print "Big list!"
        else:
            print "Short list."
test_for_type(100)
test_for_type("Wuddup")
test_for_type([2, 5, 9])