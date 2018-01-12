
# Write a function that takes the multiply function call as an argument. Your new function should return 
# the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number 
# in the original list. Here's an example:

def odd_even():
    i = 1
    while (i <= 2000):
        if (i % 2 == 0):
            print str(i) + " Even number."
        else:
            print str(i) + " Odd number."
        i +=1
odd_even()


a = [2, 4, 10, 16]
def multiply(lst, num):
    new_lst = []
    for val in lst:
        new_lst.append(val*num)
    return new_lst
print multiply(a, 5)

def layered_multiples(arr):
    new_array = []
    for item in arr:
        counter = 0
        value_list = []
        while (counter < item):
            value_list.append(1)
            counter +=1
        new_array.append(value_list)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
