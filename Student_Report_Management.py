# STUDENT MANAGEMENT SYSTEM

print("--- WELCOME TO STUDENT REPORT CARD MANAGEMENT SYSTEM ---")
print("\n--- PLEASE ENTER THE ASKED DATA ---")
s1,s2,s3 = input("\nEnter 3 subject names : ").split()
student_dictionary = {}
total_marks_list = []
fail_student_list = []
while True:
    marks_list  = []
    info_list = []
    _list = []
    name = input("Enter name of student : ")
    roll = int(input("Enter roll number of student : "))
    marks_list = list(map(int,input(f"Enter marks in {s1}, {s2} and {s3} : ").split()))
    if marks_list[0]<32 or marks_list[1]<32 or marks_list[2] < 32 :
        fail_student_list.append(name)
    total_marks_list.append(sum(marks_list))
    _list.append(roll)
    _list.append(marks_list)
    info_list.append(_list)
    student_dictionary.update({name:info_list})
    print("\nWant to continue ? No - > N : ")
    choice = input("Enter your choice : ")
    if choice.lower() == 'n' :
        break
    
topper_marks = max(total_marks_list)
while True :
    print("\nWant to know topper ? ")
    choice = input("Enter choice : YES - 'Y' : ")
    if choice.upper() == 'Y':
        for key,value in student_dictionary.items():
            if topper_marks == sum(value[0][1]):  
                print(f"\n... TOPPER : {key} .... ")
        break
    break
    
while True:
    print("\nWant to search student by roll_number ? ")
    choice = input("Enter choice : YES - 'Y' : ")
    if choice.upper() == 'Y':
        roll = int(input("Enter roll number to search  : "))
        for key,value in student_dictionary.items():
            if roll in value[0]:
                print("\n... STUDENT FOUND ...")
                print(f"Name : {key}")
            else:
                print("\n... STUDENT NOT FOUND ....")
    else:
        break

print("\nWant to view failed students ? YES - 'Y' ")
choice = input("Enter choice : YES - 'Y' : ")
if choice.upper() == 'Y':
    print("\n... FAILED STUDENTS ... ")
    print(fail_student_list)

while True :
    print("\nWant to update marks of student ? No - 'N' : ")
    choice = input("Enter choice : ")
    if choice.lower() == 'n':
        break
    roll = int(input("Enter rollnumber of student : "))
    for key,value in student_dictionary.items():
        if roll in value[0]:
            print("... STUDENT FOUND ...")
            print(f"Name : {key}")
            marks_list  = []
            info_list = []
            _list = []
            marks_list = list(map(int,input(f"Enter new marks in {s1}, {s2} and {s3} : ").split()))
            if marks_list[0]<32 or marks_list[1]<32 or marks_list[2] < 32 :
                fail_student_list.append(name)
            total_marks_list.append(sum(marks_list))
            _list.append(roll)
            _list.append(marks_list)
            info_list.append(_list)
            student_dictionary.update({name:info_list})
        else:
            print("... STUDENT NOT FOUND ....")

while True:
    print("\nWant to view student's report card ? YES -'Y' : ")
    choice = input("Enter choice : YES - 'Y' : ")
    if choice.upper() == 'Y':
        roll = int(input("Enter roll number of student : "))
        for key,value in student_dictionary.items():
            if roll == value[0][0]:
                print("\n--- STUDENT FOUND ---")
                print("--- VIEWING REPORT CARD ---\n")
                print("\n          --- MARKSHEET ---")
                percentage = sum(value[0][1])/300
                if key in fail_student_list:
                    pass_condition = "FAIL"
                else:
                    pass_condition = "PASS"
                marks_list = value[0][1]
                print(f"+-------------------------------------+")
                print(f"| Name : {key:<28} |")
                print(f"+-------------------------------------+")
                print(f"| Roll Number : {value[0][0]:<22}|")
                print(f"+-------------------------------------+")
                print(f"| Percentage : {percentage*100:.2f}%{'':15}  |")
                print(f"+-------------------------------------+")
                print(f"| Pass Condition : {pass_condition:<17}  |")
                print(f"+-------------------------------------+")
                print(f"|{'S.N.':6} | {' SUBJECT':15}  | {' MARKS':9}|")
                print(f"+-------------------------------------+")
                print(f"|{' 1.':6} |  {s1:<15} |{marks_list[0]:<10}|")
                print(f"+-------------------------------------+")
                print(f"|{' 2.':6} |  {s2:<15} |{marks_list[1]:<10}|")
                print(f"+-------------------------------------+")
                print(f"|{' 3.':6} |  {s3:<15} |{marks_list[2]:<10}|")
                print(f"+-------------------------------------+")
    else:
        break

print("--- EXITING SYSTEM ---\n")
exit()
    
            
    



