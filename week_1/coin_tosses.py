# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times 
# the head/tail appears.

import random
random.randint(60, 100)

def coin_toss_simulator():
    counter = 1
    while (counter <= 5000):
        side = random.randint(1, 2)
        if (side % 2 == 0):
            print "Attempt number " + str(counter) + ". It's heads!"
        else:
            print "Attempt number " + str(counter) + ". It's tails!"
        counter +=1
coin_toss_simulator()