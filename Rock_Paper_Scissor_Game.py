import random as r

print("\n--- WELCOME TO ROCK PAPER SCISSOR GAME ---")
while True :
    print("\n+----------+----------+")
    print(f"|{'Options':10}|{'Numbers':10}|")
    print("+----------+----------+")
    print(f"|{'Rock':10}|{' 1.':10}|")
    print("+----------+----------+")
    print(f"|{'Paper':10}|{' 2.':10}|")
    print("+----------+----------+")
    print(f"|{'Scissor':10}|{' 3.':10}|")
    print("+----------+----------+\n")

    list_choice = [1,2,3]
    while True :
        user_choice = int(input("Enter choice : "))
        if user_choice <1 or user_choice >3:
            print("--- INVALID CHOICE ---")
            print("--- RE-ENTER ---")
        else:
            break

    computer_choice= r.choice(list_choice)

    if user_choice == 1 :
        if computer_choice == 1:
            print("... DRAW ...")
            print("Computer move : Rock ")
        
        if computer_choice == 2:
            print("... COMPUTER WON ...")
            print("Computer move : Paper ")
        
        if computer_choice == 3:
            print("... USER WON ...")
            print("Computer move : Scissor ")

    if user_choice == 2 :
        if computer_choice == 1:
            print("... USER WON ...")
            print("Computer move : Rock ")
        
        if computer_choice == 2:
            print("... DRAW ...")
            print("Computer move : Paper ")
        
        if computer_choice == 3:
            print("... COMPUTER WON ...")
            print("Computer move : Scissor ")

    if user_choice == 3 :
        if computer_choice == 1:
            print("... COMPUTER WON ...")
            print("Computer move : Rock ")
        
        if computer_choice == 2:
            print("... USER WON ...")
            print("Computer move : Paper ")
        
        if computer_choice == 3:
            print("... DRAW ...")
            print("Computer move : Scissor ")

    print()
    print("\n+----------+----------+")
    print(f"|{'Options':10}|{'Numbers':10}|")
    print("+----------+----------+")
    print(f"|{'PLAY':10}|{' 1.':10}|")
    print("+----------+----------+")
    print(f"|{'EXIT':10}|{' 2.':10}|")
    print("+----------+----------+\n")

    while True :
        choice = int(input("Enter choice : "))
        if choice !=1 and choice !=2:
            print("--- INVALID CHOICE ---")
            print("--- RE-ENTER ---")

        else:
            break
    
    if choice == 2:
        print("--- EXITING GAME ---")
        print("--- GOOD BYE ---")
        print()
        exit()



    


    


