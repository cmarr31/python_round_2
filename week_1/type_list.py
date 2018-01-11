
l = ['magical unicorns',19,'hello',98.98,'world']


def type_list(list1):
    new_str = ""
    running_sum = 0
    num_of_strings = 0
    num_of_integers = 0
    for i in list1:
        if (type(i) is str):
            new_str +=i
            num_of_strings +=1
        elif (type(i) is int):
            running_sum +=i
            num_of_integers +=1
    print sum
    print new_str
    print "There are " + str(num_of_integers) + " numbers and " + str(num_of_strings) + " strings."
    if (num_of_integers == 0):
        print "This list is completely comprised of strings."
    elif (num_of_strings == 0):
        print "This list is completely comprised of integers."
    else:
        print "Mixed."

type_list(l)