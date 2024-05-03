#this is the module file the main code is in the file named project.py
import sys
import datetime
# Files used
equipmentfile = "equipment.txt"
login_staff = "login_staff.txt"
login_students = "login_students.txt"
login_visitor = "login_visitor.txt"
borrowed_file = "borrowed.txt"

# This function takes the input for the Equipment 
def equipments():
    i=1
    print("Choose an equipment :\n")
    with open(equipmentfile, "r") as file:
        for line in file:
            columns = line.strip().split(",")
            print(f"{i}. "+columns[0])
            i+=1
    equip=input("-->")
    return equip

# This function is used to sign up staff member
def write_login_credentials_staff(username, password):
    with open(login_staff, "a") as file:
        file.write(f"{username},{password}\n")

# This function is used to sign up student
def write_login_credentials_stud(username, password):
    with open(login_students, "a") as file:
        file.write(f"{username},{password}\n")

# This function is used to sign up a visitor
def write_login_credentials_visitor(username, password):
    with open(login_visitor, "a") as file:
        file.write(f"{username},{password}\n")

# This function reads the login credentials from file of staff members
def read_login_credentials_staff():
    login_credentials = {}
    with open(login_staff, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            login_credentials[username] = password
    return login_credentials

# This function is used to read the login credentials from file of students
def read_login_credentials_stud():
    login_credentials = {}
    with open(login_students, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            login_credentials[username] = password
    return login_credentials

# This function is used to read the login credentials from file of visitors
def read_login_credentials_visitor():
    login_credentials = {}
    with open(login_visitor, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            login_credentials[username] = password
    return login_credentials

# This function takes the input of the login credentials from the user
def login(login_credentials):
    i = 0
    username = input("USERNAME: ")
    while i < 3:
        password = input("PASSWORD: ")
        if username in login_credentials and login_credentials[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid login ID or Password")
            i += 1
    if i == 3:
        sys.exit()

# This function is used to borrow an equipment 
def borrow_equipment(username, equipment):
    current_time = datetime.datetime.now()
    borrow_date = current_time.date()
    borrow_time = current_time.time()
    borrow_day = borrow_date.strftime("%A")

    with open(borrowed_file, "a") as file:
        file.write(f"{username},{equipment},{borrow_date},{borrow_time},{borrow_day}\n")

    print(f"{equipment} borrowed successfully by {username} on {borrow_date} at {borrow_time} ({borrow_day})")

    # Decrease the count of equipment in equipment file
    with open(equipmentfile, "r") as f:
        lines = f.readlines()
    with open(equipmentfile, "w") as f:
        for line in lines:
            item, count = line.strip().split(",")
            if item == equipment:
                count = str(int(count) - 1)
            f.write(f"{item},{count}\n")

# This function is used to return a borrowed equipment
def return_equipment(username, equipment):
    current_time = datetime.datetime.now()
    return_date = current_time.date()
    return_time = current_time.time()

    with open(borrowed_file, "r") as file:
        lines = file.readlines()

    with open(borrowed_file, "w") as file:
        for line in lines:
            if not line.startswith(f"{username},{equipment}"):
                file.write(line)

    print(f"{equipment} returned successfully by {username} on {return_date} at {return_time}")

    # Increase the count of equipment in equipment file
    with open(equipmentfile, "r") as f:
        lines = f.readlines()

    with open(equipmentfile, "w") as f:
        for line in lines:
            item, count = line.strip().split(",")
            if item == equipment:
                count = str(int(count) + 1)
            f.write(f"{item},{count}\n")

# This function is used to add a new equipment to the equipment list
def add_equipment(equipment_name, initial_count):
    with open(equipmentfile, "a") as file:
        file.write(f"{equipment_name},{initial_count}\n")
    print(f"{equipment_name} added successfully with count {initial_count}")

# Sign up function
def Sign_Up():
    opt = input("1. Staff\n2. Student\n3. Visitor\n--> ")
    if opt == '1':
        username = input("PLEASE ENTER YOUR USERNAME: ")
        password = input("PLEASE ENTER THE PASSWORD TO BE SET FOR YOUR ACCOUNT: ")
        write_login_credentials_staff(username, password)
        Task(username)
    elif opt == '2':
        username = input("PLEASE ENTER YOUR USERNAME: ")
        password = input("PLEASE ENTER THE PASSWORD TO BE SET FOR YOUR ACCOUNT: ")
        write_login_credentials_stud(username, password)
        issue(username)
    elif opt == '3':
        username = input("PLEASE ENTER YOUR USERNAME: ")
        password = input("PLEASE ENTER THE PASSWORD TO BE SET FOR YOUR ACCOUNT: ")
        write_login_credentials_visitor(username, password)
        issue(username)
    else:
        print("Invalid input!!")
        ch = input("Do you want to change the input? (y/n): ")
        if ch.lower() == 'y':
            Sign_Up()
        elif ch.lower() == 'n':
            print("Thank you for visiting, Have a nice day!")
            sys.exit()
        else:
            print("Invalid choice!")
            sys.exit()

def Task(username):
    while True:
        print("\nChoose an action:")
        print("1. Add existing equipment")
        print("2. Add a new equipment")
        print("3. Issue an equipment")
        print("4. Equipments Currently issued")
        print("5. Exit")
        option = input("--> ")

        if option == '1':
            equipment = input("Enter the equipment you want to add : ")
            f_count = int(input("Enter how many to add : "))
            with open(equipmentfile, "r") as f:
                lines = f.readlines()
            with open(equipmentfile, "w") as f:
                for line in lines:
                    item, count = line.strip().split(",")
                    if item == equipment:
                        count = str(int(count) + f_count)
                    f.write(f"{item},{count}\n")
                print("Equipments Increased !")
        
        elif option == '2':
            equip_name = input("Enter the name of the equipment : ")
            init_count = int(input("Enter the initial count of the equipment :"))
            add_equipment(equip_name, init_count)
        
        elif option == '3':
            q = input("Choose an Action\n1. Borrow\n2. Return\n--> ")
            if q == '1':
                equip = equipments()
                if equip in '1234':
                    borrow_equipment(username, equip)
                else:
                    print("Invalid equipment choice")
            
            elif q == '2':
                equip = equipments()
                if equip in ["1", "2", "3", "4"]:
                    return_equipment(username, equip)
                else:
                    print("Invalid equipment choice")
            else:
                print("Invalid input")
        
        elif option == '4':
            with open(borrowed_file, "r") as file:
                content = file.read()
                if len(content) == 0:
                    print("No equipment issued !")
                else:
                    print(content)
        elif option == '5':
            print("Thank you !")
            sys.exit()
        else:
            print("Invalid input")
def issue(username):
    while(True):
        equi=equipments()
        choice=int(input("Chosse an action:\n1. Borrow \n2.Return\n3.Exit\n-->"))
        if choice == 1:
            borrow_equipment(username,equi)
        elif choice == 2:
            return_equipment(username, equi)
        else:
            sys.exit()
def desig():
    design=int(input("1. Student\n2. Staff\n3. Visitor\n-->"))
    return design
