students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(list):
    for person in list:
        print person["first_name"] + " " + person["last_name"]

# names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_and_instructors(dictionary):
    for title in dictionary:
        print title
        counter = 0
        for person in dictionary[title]:
            counter +=1
            first_name = person["first_name"]  
            last_name = person["last_name"]
            length = len(first_name) + len(last_name)
            print "{}-{} {}-{}".format(counter, first_name, last_name, length)
            
students_and_instructors(users)