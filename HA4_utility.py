#utility HA4
def create_dict(studentProfile):
    students = {}
    #your code here
    #read the file - obtain the key and value information
    #create the dictionary
    with open(studentProfile, 'r') as f:
        for line in f:
            student_id, name, email, major, cgpa = line.strip().split('|')
            k = student_id #key
            v = [name, email, major, cgpa] #value
            students[k] = v #creates dictionary
    return students

def add(students):
    '''
    returns True if student added
    otherwise returns False
    '''
    #your  code here
    student_id = input('Enter student ID to add: ')
    if student_id not in students:
        name = input('Enter full name: ') #asks for name
        email = input('Enter email address: ') #asks for email
        major = input('Enter major: ') #asks for major
        cgpa = input('Enter student CGPA: ') #asks for cgpa
        students[student_id] = [name, email, major, cgpa]
        return True
    else:
        return False

def display(students):
    '''prints a dictionary'''
    for k, v in students.items():
        line = '{}|{}'.format(k, '|'.join(v))
        print(line)   

def search(students, student_id):
    '''returns dict value if student ID (key) found
    otherwise returns a False'''
    #your code here
    if student_id in students:
        return students[student_id]
    else:
        return False
    

def update(students, student_id, field, value):
    '''returns True if item updated
    otherwise returns False'''

    # your code here
    if student_id in students:
        fields = ['name', 'email', 'major', 'cgpa']
        index = fields.index(field)
        students[student_id][index] = value
        return True
    else:
        return False

def delete(students, student_id):
    '''returns True if item deleted
    otherwise returns False'''
    #your code here
    if student_id in students:
        del students[student_id] #deletes respective item
        return True
    else:
        return False