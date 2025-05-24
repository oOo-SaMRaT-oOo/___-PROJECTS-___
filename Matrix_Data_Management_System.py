import numpy as np

class DatasetManager():
    def __init__(self,filename,list_elements,row,cols):
        self.filename = filename
        self.list_elements = list_elements
        self.row = row
        self.cols = cols
        return

    def add_data(self):
        self.list_elements = np.array(self.list_elements).reshape(self.row,self.cols)
        return

    def save_to_file(self):
        np.savetxt(self.filename,self.list_elements)
        return

    def load_from_file(self):
        return np.loadtxt(self.filename)
    
    def compute_statistics(self):
        matrix = self.load_from_file()
        if self.row==self.cols:
             print("\n\nMatrix is square")
             print("... Computed Statistics ...")
             print("Mean deviation :",round(np.mean(matrix),3))
             print("Standard deviation :",round(np.std(matrix),3))
             print("Determinent :",round(np.linalg.det(matrix)))
        else:
            print("Matrix is not Square ")

    def matrix_features(self):
        matrix = self.load_from_file()
        print("Transpose matrix :\n",np.transpose(matrix))
        if np.linalg.det(matrix) ==0:
            print("Matrix is singular ")
            print("No inverse ")
        else:
            print("Inverse Matrix :\n",np.linalg.inv(matrix))        
        
        
    
    def display_matrix(self):
        matrix = self.load_from_file()
        print("Given matrix :\n",matrix)

    def reset_system(self):
        with open(self.filename,"w") as f:
            f.close()

# file_name = input("Enter file name to save : ")

while True :
    print("\n... WELCOME TO DATASET MANAGING SYSTEM ...\n")
    print("+----------+--------------------+")
    print(f"| {"NUMBER":9}|{"ACTION TO PERFORM":19} |")
    print("+----------+--------------------+")
    print(f"| {"1.":9}|{"Input DATA Matrix":19} |")
    print("+----------+--------------------+")
    print(f"| {"2.":9}|{"See Matrix Features":19} |")
    print("+----------+--------------------+")
    print(f"| {"3.":9}|{"See Matrix Stats ":19} |")
    print("+----------+--------------------+")
    print(f"| {"4.":9}|{"Show Given Matrix ":19} |")
    print("+----------+--------------------+")
    print(f"| {"5.":9}|{"EXIT":19} |")
    print("+----------+--------------------+")

    choice = int(input("\nEnter choice : "))
    while True :
        if choice<1 or choice >5 :
            print()
            print("... Invalid choice ...")
            choice = int(input("Enter choice : "))
        else:
            break

    if choice ==1 :
        data = list(map(int,input("\nEnter elements of matrix : ").split()))
        row,cols = map(int,input("Enter order of matrix : ").split())
        dataset = DatasetManager("dataset.txt",data,row,cols)
        dataset.add_data()
        dataset.save_to_file()
        dataset.load_from_file()

    if choice == 2 :
        dataset.matrix_features()

    if choice == 3:
        dataset.compute_statistics()
        
    if choice == 4:
        dataset.display_matrix()

    if choice == 5:
        print("\n... THANK YOU USER ...")
        print("... BYE ...\n")
        exit()

    print("\n................\n")
    print("+----------+--------------------+")
    print(f"| {"1.":9}|{"EXIT SYSTEM":19} |")
    print("+----------+--------------------+")
    print(f"| {"2.":9}|{"PERFORM FUNCTIONS":19} |")
    print("+----------+--------------------+")

    choice_f = int(input("\nEnter choice -> "))

    while True :
        if choice_f !=1 and choice_f !=2:
            print("... Invalid choice ...")
            choice_f = int(input("\nEnter choice -> "))
        else:
            break
    
    if choice_f == 1:
        print("\n... THANK YOU USER ...")
        print("... BYE ...\n")
        exit()

    print("\n................")
    









    
    

         


    