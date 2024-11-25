#application HA4
import Christopher_Faustino_HA4_utility as u

def main():
    students = u.create_dict('studentProfile.txt') #create dict from file
    u.display(students) #display dict content
        
    menu = '\n\n[a] Add\n[s] Search\n[u] Update\n[d] Delete\n[dis] Display\n[exit] Exit'
    choice = ''
    while choice!= 'exit':
        print(menu)
        choice = input('\nEnter your choice: ') #asks for choice
        
        if choice == 'a': #add
            if u.add(students):
                print('Student information added')
            else:
                print('Student already exist')
                
        elif choice == 's': #search
            #your code here
            student_id = input('Enter student ID to search: ') #asks student to search for
            student = u.search(students, student_id)
            if student:
                print(f"\n{student[0]}-{student[1]}-{student[2]}-{student[3]}")
            else:
                print('Student not found.')          
                    
        elif choice == 'u': #update
            #your code here
            student_id = input('Enter student ID to update: ') #asks for student to update
            field = input('Which one to update (name/email/major/cgpa)? ') #asks which field to update
            value = input('Enter updated info: ') #asks new info
            if u.update(students, student_id, field, value):
                print('Information Updated.')
            else:
                print('Unable to update. Student ID or field not found.')
                    
        elif choice == 'd': #delete
            #your code here
            student_id = input('Enter student ID to delete: ') #asks for student to delete
            if u.delete(students, student_id):
                print('Record Deleted.')
            else:
                print('Student not found.')
                
        elif choice == 'dis': #display
            #your code here
            u.display(students)
            
        elif choice == 'exit': #exit
            print('Exiting application.')
        else:
            print('Invalid option. Return to main menu.')
         
        
main()