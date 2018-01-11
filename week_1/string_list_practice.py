
import string

words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")

new_str = string.replace(words, "day", "month")
print new_str

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]

def first_and_last(lst):
    new_lst = []
    new_lst.append(lst[0])
    new_lst.append(lst[-1])
    print new_lst
first_and_last(y)

yyz = [19,2,54,-2,7,12,98,32,10,-3,6]

yyz.sort()
def split(original_lst):
    #new_list = []
    half = len(original_lst)/2
    first_half = original_lst[:half]
    second_half = original_lst[half:]
    #new_list.append(second_half)
    #new_list.append(first_half)
    #print new_list
    #second_half.insert(0, first_half)
    #print new_list
    second_half.insert(0, first_half)
    print second_half
split(yyz)