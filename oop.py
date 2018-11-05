# #1: Define a Vehicle class with the following attributes and methods: 
# - `vehicle_type` 'str'
# - `wheel_count` 'int'
# - `name` 'str'
# - `cost` 'int'
# - `colors` 'str'
# - `vehicle_brand` 'str'
# - `mpg` 'dict', with the following properties:
#     - `city` 'int'
#     - `highway` 'int'
#     - `combined` 'int'
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_drive` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_drive  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. The methods should be defined on the class.



# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `pop_wheelie` 'bool', if `wheel_count` is not equal to 2 then it should be
#   False



# #3: Define a Car class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `can_drive` that should return 'Vrrooooom Vroooom'



# #4: Define a Truck class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `rev_engine` that should return 'revvvvvreeeev'



# Commit when you finish working on these questions!

class Vehicle(object):
    def __init__(self, vehicle_type, wheel_count, name, cost, colors, vehicle_brand, mpg):
        self.vehicle_type = str
        self.wheel_count = int


class Motorcycle(Vehicle):
    def __init__(self, wheel_drive):
        self.wheel_drive = str
        # super(Motorcycle, self).__init__(self, wheel_drive, wheel_count)
        # self.wheel_count = 2

    def pop_wheelie(bool):
        if wheel_count != 2:
            return False


class Car(Vehicle):
    def __init__(self, wheel_drive):
        self.wheel_drive = str
    def can_drive(self):
        return 'Vrrooooom Vroooom'


class Truck(Vehicle):
    def __init__(self, wheel_drive):
        self.wheel_drive = str

    def rev_engine(self):
        return 'revvvvvreeeev'
