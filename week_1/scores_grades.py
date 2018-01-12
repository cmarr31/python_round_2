import random

# Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
# your function should display what the grade is for a particular score.
def scores_and_grades():
    counter = 0
    while (counter < 10):
        random_num = random.randint(60, 100)
        if (random_num < 70):
            print str(random_num) + " Grade - D."
        elif (random_num < 80):
            print str(random_num) + " Grade - C."
        elif (random_num < 90):
            print str(random_num) + " Grade - B."
        elif (random_num <= 100):
            print str(random_num) + " Grade - A."
        counter +=1
scores_and_grades()