
def print_odds():
    num = 1
    while (num < 1000):
        print num
        num +=2
print_odds()

def print_mults_5():
    num2 = 5
    while (num2 < 1000005):
        print num2
        num2 +=5
print_mults_5()

a = [1, 2, 5, 10, 255, 3]
def sum_of_list(lst):
    print sum(lst)
sum_of_list(a)

def average_of_list(lst):
    print sum(lst)/len(lst)
average_of_list(a)