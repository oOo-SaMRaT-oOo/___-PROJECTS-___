class Complex_Number():
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,obj2):
        new_real = self.real + obj2.real
        new_img = self.img + obj2.img
        return Complex_Number(new_real,new_img)
    
    def __sub__(self,obj2):
        new_real = self.real - obj2.real
        new_img = self.img - obj2.img
        return Complex_Number(new_real,new_img)
    
    def __eq__(self,obj2):
        if self.real == obj2.real and self.img == obj2.img:
            return True
        return False
    
    def show_number(self):
        print(f"Complex number : {self.real} + {self.img} i")
    

print("\n\n... WELCOME TO SIMPLE COMPLEX CALCULATOR...\n")
print("ENTER THE DATA :")
r1,i1 = map(int,input("Enter real and img part of 1st complex number : ").split())
r2,i2 = map(int,input("Enter real and img part of 2nd complex number : ").split())
obj1 = Complex_Number(r1,i1)
obj2 = Complex_Number(r2,i2)

while True:
    print()
    while True:
        print("+----------+---------------+")
        print(f"|{"NUMBER":10}|{"ACTION":15}|")
        print("+----------+---------------+")
        print(f"|{" 1.":10}|{"ADDITION":15}|")
        print("+----------+---------------+")
        print(f"|{" 2.":10}|{"SUBTRACTION":15}|")
        print("+----------+---------------+")
        print(f"|{" 3.":10}|{"CHECK EQUALITY":15}|")
        print("+----------+---------------+")
        print(f"|{" 4.":10}|{"EXIT":15}|")
        print("+----------+---------------+")

        choice =  int(input("\nEnter choice : "))
        if choice >=1 and choice <=4:
            break

    if choice == 1:
        add_num = obj1 + obj2
        add_num.show_number()

    if choice == 2:
        sub_num = obj1 - obj2
        sub_num.show_number()

    if choice == 3:
        if(obj1 == obj2):
            print("Complex number are equal ... !")
        else:
            print("Complex Number are not equal ... !")
        
    if choice == 4:
        print("\n...THANK YOU USER ...\n")
        exit()

    print("\n\n...\n")
    print("+----------+---------------+")
    print(f"|{"NUMBER":10}|{"ACTION":15}|")
    print("+----------+---------------+")
    print(f"|{" 1.":10}|{"PERFORM":15}|")
    print("+----------+---------------+")
    print(f"|{" 2.":10}|{"LEAVE":15}|")
    print("+----------+---------------+")
    print()
    choice2 = int(input("Enter choice : "))
    if choice2 == 2:
        print("\n...THANK YOU USER ...\n")
        exit()
        
        




