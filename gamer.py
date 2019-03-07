def main():
    lastName = ""
    firstName = ""
    phoneNum = ""
    choice = None

    while True:
        try:
            inEmployFile = open("employee.dat", "r")
            inEmployFile.close()
            break
        except FileNotFoundError:
            print ("File could not be opened.")
            inEmployFile = open("employee.dat", "w")

    while choice != "0":
        print(
        """
        Employees
        
        0 - Quit
        1 - List names
        2 - Add an employee
        3 - Remove an employee
        """
        )
        choice = input("Choice: ")
        print()
        # exit
        if choice == "0":
            print("Good-bye.")
        # displays employees
        elif choice == "1":
            print("EMPLOYEE LIST\n")
            print("LAST NAME\tFIRST NAME\tPHONE NUMBER\n")
            inEmployFile = open("employee.dat", "r")
            inEmployFile.readlines()
            for line in inEmployFile:
                print(line)
            inEmployFile.close()
        # add an employee
        elif choice == "2":
            lastName = input("What is the employee's last name?: ")
            firstName = input("What is the employee's first name?: ")
            phoneNum = input("What is the employee's phone number?: ")
            entry = (lastName+"\t"+firstName+"\t"+phoneNum+"\n")
            print(entry)
            inEmployFile = open("employee.dat", "a")
            inEmployFile.writelines(entry)
            inEmployFile.close()
        # delete an employee
        elif choice == "3":
            score = int(input("What is the score you want to remove?"))
            name = input("What is the name of the person you want me to delete?")
            entry = score, name
            names.remove(entry)
            print("I deleted", entry, "score!")
        # some unknown choice
        else:
            print("Sorry, but", choice, "isn't a valid choice.")

    input("\n\nPress the enter key to exit.")
main()
