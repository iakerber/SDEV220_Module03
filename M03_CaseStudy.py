#Ilze Akerbergs
#M03_CaseStudy.py
#create class Vehicle and inherit that into class Automobile, create year, make, model, doors, roof attributes, input and print out
class Vehicle():
    def __init__(self):
        self.vehicle_type = None
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
	
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
def main():
    car = Automobile()
    vehicle_type = "car"
    year = input("What year is the car? ")
    make = input("What is the make of the car? ")
    model = input("What is the model of the car? ")
    doors = input("How many doors does the car have? ")
    roof = input("What type of roof does the car have? ")
    car.set_vehicle_type(vehicle_type)
    car.set_attributes(year, make, model, doors, roof)
    print("\nCar Details: ","\nVehicle type: ",vehicle_type,"\nYear: ",year,"\nMake: ",make,"\nModel: ",model,"\nNumber of doors: ",doors,"\nType of roof: ",roof)
    car.set_attributes(year, make, model, doors, roof)
if __name__== "__main__":

    main()
