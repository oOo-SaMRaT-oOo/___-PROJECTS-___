print("\n\n\n... WELCOME TO CONTACT BOOK SYSTEM ...\n")

while True :
    print("\n\n--- DEAR USER ENTER CHOICE ---")
    print("+--------+-------------------+")
    print(f"| {"NUMBER":6} | {"ACTION":18}|")
    print("+--------+-------------------+")
    print(f"| {" 1.":6} | {"ADD CONTACT":18}|")
    print("+--------+-------------------+")
    print(f"| {" 2.":6} | {"VIEW CONTACT":18}|")
    print("+--------+-------------------+")
    print(f"| {" 3.":6} | {"SEARCH CONTACT":18}|")
    print("+--------+-------------------+")
    print(f"| {" 4.":6} | {"EXIT SYSTEM":18}|")
    print("+--------+-------------------+")

    while True :
        choice = int(input("\nPlease enter your choice : "))
        if choice<1 or choice>4 :
            print("... Invalid input ... ")
            print("... Re-enter your input ... ")
            choice = int(input("Please enter your choice as per above : "))        
        else:
            break

    if choice == 1:
        try :
            with open("contact.txt","a") as f:
                name = input("Enter name : ")
                phone_number = input("Enter phone number : ")
                string_to_write = f"{name}, {phone_number}\n"
                f.write(string_to_write)

        except FileNotFoundError :
            print("\n--- FILE NOT FOUND ERROR ---")

    if choice == 2:
        try :
            with open("contact.txt","r") as f:
                line_list = f.readlines()
                print("\n--- CONTACT DATA ---\n")
                for line in line_list:
                    line = line.replace("\n","")
                    name_num_list = line.split(",")
                    name_num_list[0] = name_num_list[0].lstrip()
                    name_num_list[1] = name_num_list[1].lstrip()
                    print(name_num_list)

        except FileNotFoundError :
            print("\n--- FILE NOT FOUND ERROR ---")


    if choice == 3:
        name = input("\nEnter name of person to search : ")
        try :
            with open("contact.txt","r") as f:
                line_list = f.readlines()
                for line in line_list:
                    line = line.replace("\n","")
                    name_num_list = line.split(",")
                    name_num_list[0] = name_num_list[0].lstrip() # Name
                    name_num_list[1] = name_num_list[1].lstrip() # Number
                    if name.lower() == name_num_list[0].lower():
                        print("\n--- CONTACT FOUND ---")
                        print("Name :",name_num_list[0])
                        print("Phone number :",name_num_list[1])

        except FileNotFoundError :
            print("\n--- FILE NOT FOUND ERROR ---")

    if choice == 4:
        print("\n--- THANK YOU ---")
        print("--- EXITING SYSTEM ----\n")
        exit()


        


            

