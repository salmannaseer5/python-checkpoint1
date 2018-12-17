# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.

class Vehicle: 
    def __init__(self, veicle_type, wheel_count, name):
        self.vehicle_type= vehicle_type
        self.wheel_count= wheel_count
        self.name= name
        self.cost= cost
        self.color= colors
        self.vehicle_brand= vehicle_brand
        self.mpg= {
            city: '',
            highway: '',
            combined:''
        }

# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"

class Motorcycle(Vehicle):
    def __init__(self, wheel_count):
    super().__init__(wheel_count)
        self.wheel_count= "no wheels!"

    def pop_wheelie(pop):
        if wheel_count != 2
        return False
        else 
        print("......Pop")

# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
    def __init__(self, wheel_count):
        super().__init__(wheel_count)
        self.wheel_count= 4

    def can_drive(vroom):
        return 'Vrrooooom Vroooom'

# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'

class Truck(Vehicle):
    def __init__(self, wheel_count):
        super().__init__(wheel_count)
        self.wheel_count= "no wheels!"

        def rev_engine(rev):
            return 'revvvvvreeeev'


# Commit when you finish working on these questions!