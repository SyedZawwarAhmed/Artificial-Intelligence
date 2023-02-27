def getData():
    city = input("Enter city name:- ")
    population = int(input("Enter city population:- "))
    mayor = input("Enter city mayor:- ")
    return {
        "city": city,
        "population": population,
        "mayor": mayor
    }

def writeData(data):
    file = open("cityData.csv", "a")
    file.write(f'{data["city"]},{data["population"]},{data["mayor"]}\n')
    file.close()

numberOfCities = int(input("Enter number of cities you want to store data of:- "))

for i in range(numberOfCities):
    data = getData()
    writeData(data)