def allCars(listOfCars) :
    if type(listOfCars) == list :
        print(listOfCars)
    else :
        return "argument must be a list"

def searchCar(search,listOfCars) :
    if type(listOfCars) == list :
        searchList = []
        for car in listOfCars :
            if search in car :
                searchList.append(car)
            else :
                continue    
    else :
        return "argument must be a list"
    return searchList

def addCar(carName , listOfCars) :
    listOfCars.append(carName)
    return listOfCars

def updateCar(carName,listOfCars,update) :
    if carName in listOfCars :  
        listOfCars[listOfCars.index(carName)] = update
    else :
        return "car not found"
    return listOfCars

def deleteCar(carName,listOfCars) :
    if carName in listOfCars :  
        listOfCars.remove(carName)
    else :
        return "car not found"
    return listOfCars

