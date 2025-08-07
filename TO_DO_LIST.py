# To do list 

def add_task(task_list,task_name):
    task_list.append(task_name)

def return_pending_tasks(task_dictionary_list):
    return_list = []
    for dictionary in task_dictionary_list:
            if dictionary["TASK COMPLETION"] == False:
                return_list.append(dictionary["TASK NAME"])
    return return_list

def make_complete(task_dictionary_list):
    for dictionary in task_dictionary_list:
            dictionary.update({"TASK COMPLETION":True})

def search_task_(search_task,task_dictionary_list):
     for dictionary in task_dictionary_list:
          if search_task == dictionary["TASK NAME"]:
               print("\n\n--- TASK FOUND ---")
               print("COMPLETION STATUS :",dictionary["TASK COMPLETION"])

def check_exist(task,task_dictionary_list):
    condition = False
    for dictionary in task_dictionary_list:
        if task in dictionary["TASK NAME"]:
             condition = True
        break
    return condition
              
task_list = []
task_dictionary_list = []
task_dictionary = {}
Pending_task_list = []

while True:

    print("\n\n--- WELCOME to ' TO-DO-LIST MANAGER ' ---")
    
    while True:
        task = input("\nEnter a task  : ")
        add_task(task_list,task)

        print("\nPlease enter your choice DEAR USER :")
        print(f"+--------------+-------------+")
        print(f"| {" CHOICE":12} |{"  OPTIONS" :12} |")
        print(f"+--------------+-------------+")
        print(f"| {" ENTER MORE" :12} |{"  1." :12} |")
        print(f"+--------------+-------------+")
        print(f"| {" ENTER DONE" :12} |{"  2." :12} |")
        print(f"+--------------+-------------+")
        
        choice = int(input("\nEnter choice : "))
        if choice == 2:
            break
        else:
            continue

    print("\n\nGiven tasks : ",task_list)

    # FAULTY PART 

    ###
    if (not check_exist(task,task_dictionary_list)):
        for task in task_list:
            task_dictionary = {}
            task_dictionary.update({"TASK NAME":task})
            task_dictionary.update({"TASK COMPLETION":False})
            task_dictionary_list.append(task_dictionary)
        
    ###


    print("\nPlease enter your choice DEAR USER :")
    print(f"+----------------------+-------------+")
    print(f"| {" CHOICE":20} |{"  OPTIONS" :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" SHOW PENDING" :20} |{"  1." :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" DONT SHOW" :20} |{"  2." :12} |")
    print(f"+----------------------+-------------+")

    choice = int(input("\nEnter choice : "))
    if choice == 1:
        print("\n\nPending tasks : ",return_pending_tasks(task_dictionary_list))

    print("\nPlease enter your choice DEAR USER :")
    print(f"+----------------------+-------------+")
    print(f"| {" CHOICE":20} |{"  OPTIONS" :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" SEARCH" :20} |{"  1." :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" DONT SEARCH" :20} |{"  2." :12} |")
    print(f"+----------------------+-------------+")

    choice = int(input("\nEnter choice : "))

    if choice == 1:
        search_task = input("\n\nEnter the task to search : ")
        search_task_(search_task,task_dictionary_list)


    print("\nPlease enter your choice DEAR USER :")
    print(f"+----------------------+-------------+")
    print(f"| {" CHOICE":20} |{"  OPTIONS" :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" COMPLETE ALL" :20} |{"  1." :12} |")
    print(f"+----------------------+-------------+")
    print(f"| {" DONT CHANGE" :20} |{"  2." :12} |")
    print(f"+----------------------+-------------+")

    choice = int(input("\nEnter choice : "))

    if choice == 1:
        make_complete(task_dictionary_list)
        Pending_task_list = []

    print("\nPlease enter your choice DEAR USER :")
    print(f"+--------------+-------------+")
    print(f"| {" CHOICE":12} |{"  OPTIONS" :12} |")
    print(f"+--------------+-------------+")
    print(f"| {" RE-WIND" :12} |{"  1." :12} |")
    print(f"+--------------+-------------+")
    print(f"| {" RE-SET" :12} |{"  2." :12} |")
    print(f"+--------------+-------------+")
    print(f"| {" EXIT" :12} |{"  3." :12} |")
    print(f"+--------------+-------------+")
        
    choice = int(input("\nEnter choice : "))

    if choice == 3:
        print("\n--- EXITING ---")
        print()
        exit()

    elif choice ==2 :
         task_list = []
    task_dictionary_list = []
    task_dictionary = {}
    Pending_task_list = []
         









