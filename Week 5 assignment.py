# Base Class Assignment 1
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.__battery = battery  # private attribute (encapsulation)

    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."

    # Encapsulation: using getter and setter for battery
    def get_battery(self):
        return f"Battery level: {self.__battery}%"

    def set_battery(self, new_level):
        if 0 <= new_level <= 100:
            self.__battery = new_level
        else:
            print("Invalid battery level! Must be 0–100.")

    # Method to simulate charging
    def charge(self, amount):
        self.set_battery(min(100, self.__battery + amount))


# Derived Class (Inheritance + Polymorphism)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)  # call parent constructor
        self.gpu = gpu

    # Polymorphism: Override phone_info
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.storage}GB storage and {self.gpu} GPU."

    # Extra method specific to gaming phones
    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.gpu} GPU... Battery drains faster!")
        self.set_battery(self._Smartphone__battery - 20)  # access private with name mangling


# Creating Objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 85)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 100, "Adreno 740")

# Using methods
print(phone1.phone_info())
print(phone1.get_battery())
phone1.charge(10)
print(phone1.get_battery())

print("\n" + gaming_phone.phone_info())
print(gaming_phone.get_battery())
gaming_phone.play_game("PUBG Mobile")
print(gaming_phone.get_battery())



# Base class Activity 2
class Vehicle:
    def move(self):
        # Base method (can be overridden by subclasses)
        print("The vehicle is moving...")

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on water.")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 The bicycle is pedaling along the path.")


# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # Each class has its own version of move()
