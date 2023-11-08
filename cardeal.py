class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on =  False

    def start_engine(self):
        print("Starting engine....")
        self.engine_on = True

    def make_noise(self):
        print("Beep beep!")


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")

vehicle_choice = ['bike', 'truck']
truck_list = [
    Truck('Toyota', 1000, 28000),
    Truck('Chevy', 30000, 9000),
    Truck('Ford', 15000, 12000)
]

bike_list = [
    Motorcycle('Yamaha',  1000, 5000, 190),
    Motorcycle('Honda', 2000, 3500, 180),
    Motorcycle('Kawasaki', 1500, 4000, 200)
]

vehicles_to_compare = []


while True:
    choice = input("Which would you like to view, bike or truck? ")
    if choice == 'bike':
        print("The bike selection we offer is: ")
        for i, bike in enumerate(bike_list):
            print(f'{i + 1}. {bike.make} with {bike.miles} miles and costs ${bike.price} and top speed is {bike.top_speed} mph.')

        choosebike = int(input("Which vehicle would you like to add? Enter the corresponding number: "))
        if 1 <= choosebike and choosebike <= len(bike_list):
            vehicles_to_compare.append(bike_list[choosebike - 1])
            print(f"{bike_list[choosebike - 1].make} added!")
            compare = input("Would you like to compare your vehicles now? Enter 'y' or 'n': ")
            if compare == 'y':
                print("Here are your vehicles to compare: ")
                for i, vehicle in enumerate(vehicles_to_compare):
                    if isinstance(vehicle, Motorcycle):
                        print(f'{i + 1}. {vehicle.make} with {vehicle.miles} miles and costs ${vehicle.price} and top speed is {vehicle.top_speed} mph.')
                        vehicle.make_noise()

                    elif isinstance(vehicle, Truck):
                        print(f'{i + 1}. {truck.make} with {truck.miles} miles and costs ${truck.price}.')
                        vehicle.make_noise()
                print("Thanks for visiting! Have a good one!")
                break
            elif compare != 'y' and compare != 'n':
                break




    elif choice == 'truck':
        print("The truck selection we offer is: ")
        for i, truck in enumerate(truck_list):
            print(f'{i + 1}. {truck.make} with {truck.miles} miles and costs ${truck.price}.')

        choosetruck = int(input("Which vehicle would you like to add? Enter the corresponding number: "))
        if 1 <= choosetruck and choosetruck <= len(truck_list):
            vehicles_to_compare.append(truck_list[choosetruck - 1])
            print(f"{truck_list[choosetruck - 1].make} added!")
            compare = input("Would you like to compare your vehicles now? Enter 'y' or 'n': ")
            if compare == 'y':
                print("Here are your vehicles to compare: ")
                for i, vehicle in enumerate(vehicles_to_compare):
                    if isinstance(vehicle, Motorcycle):
                        print(f'{i + 1}. {vehicle.make} with {vehicle.miles} miles and costs ${vehicle.price} and top speed is {vehicle.top_speed} mph.')
                        vehicle.make_noise()


                    elif isinstance(vehicle, Truck):
                        print(f'{i + 1}. {vehicle.make} with {vehicle.miles} miles and costs ${vehicle.price}.')
                        vehicle.make_noise()

                print("Thanks for visiting! Have a good one!")
                break
            elif compare != 'y' and compare != 'n':
                break

    else:
        print("This is an invalid statement, please try again.")








