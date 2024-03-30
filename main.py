cars = []
import functions
while True :
    userChoice = str(input("\n 1-all values \n 2-search value \n 3-add new value \n 4-update value \n 5-delete value \n 6-exit \n Enter choice :"))
    if userChoice == "1" :
        functions.allCars(cars)
    elif userChoice == "2" :
        while True :
            searchChoice = str(input("\n 1-search car \n 2-return to main menu \n Enter choice :"))
            if searchChoice == "1" :
                search = str(input("Enter car name :"))
                print(functions.searchCar(search,cars))
            elif searchChoice == "2" :
                break
            else :
                print("unknown choice")
    elif userChoice == "3" :
        while True :
            addChoice = str(input("\n 1-add car \n 2-return to main menu \n Enter choice :"))
            if addChoice == "1" :
                newCar = str(input("Enter new car name :"))
                print(functions.addCar(newCar , cars))
            elif addChoice == "2" :
                break
            else :
                print("unknown choice")
    elif userChoice == "4" :
        carName = input("Enter car name :")
        update = input("Enter the update :")
        print(functions.updateCar(carName ,cars , update))

    elif userChoice == "5" :
       carName = input("Enter car name :")
       print(functions.deleteCar(carName,cars))
    elif userChoice == "6" :
       break
    else :
        print("unknown choice")
    
