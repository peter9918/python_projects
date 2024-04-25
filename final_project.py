"""
Author: Pencov Peter
Date: 15.04.2024

Purpose of the program:

Allows user to create Cars and Bikes objects which are subclasses of Vehicles class.
Allows objects to be stored in JSON files through Json_DB class.

"""

import json
import os
import random
import abc
import string
import re
from prettytable import PrettyTable

path1 = "C://temp/"
          
class Json_DB:
    """
    Class for creating Objects, has methods to create json files
    and edit them.
    
    Attributes:
        directory (str): The directory where the JSON file is located.
        file_name (str): The name of the JSON file.
        full_path (str): The full path of the JSON file.
    """
    
    def __init__(self, directory: str, file_name: str) -> None:
        """
        Constructor method for Json_DB class

        Args:
            directory (str): Path to directory for json file. ex: "C://temp/"
            file_name (str): file name. Has to have .json extension

        Raises:
            ValueError: if path does not exist
            ValueError: if file does not have .json extension
        """
        
        if file_name.endswith(".json"):
            self.file_name = file_name
            if os.path.exists(directory):
                self.directory = directory
            else:
                raise ValueError("path to directory does not exist")
        else:
            raise ValueError("needs to be a json file (.json extension)")
             
        self.full_path = directory + file_name
        
    def __str__(self) -> str:
        """
        String method for class Json_DB
        Warns the user if a json file is not created yet for this object
            return: full path of Json_DB object, contents of Json file
        """
        try:
            with open(self.full_path, "r") as f:
                data = f.read()
        except FileNotFoundError as e:
            return f"A file was not created for this object.\
                \nObject full path: {self.full_path}\
                \nCreate a file using create_file method"
        else:
            return f"\nObject full path: {self.full_path}\
                \nfile contents:\n{data}"
                
    def create_file(self) -> None:
        """
        Creates a new JSON file if it does not exist
        or prompts the user to overwrite it if it does. 
        """
        if self.file_name in os.listdir(self.directory):
            with open(self.full_path, "r") as f:
                    print(f.read())
            
            while True:    
                choice = input("file already exists, content listed above. Sure you want to overwrite file? (y/n)").lower()
                if choice == "y":
                    print("overwriting file...")
                    with open(self.full_path, "w") as f:
                        pass
                    break
                elif choice == "n":
                    print("opperation canceled")
                    break
                else:
                    print("invalid answer. y/n")
                    continue
        else:
            with open(self.full_path, "w") as f:
                pass
            print(f"file {self.full_path} was created successfully")
            
    def write_to_file(self, *items) -> None:
        """
        Writes to existing file of Json_DB object
        If the file is empty or does not contain valid json data sets the file to empty dict before making changes
        Warns the user if a json file is not created yet for this object
         
        *items: Cars or Bikes objects. Or a list of Cars or Bikes objects  
        """
        if self.file_name not in os.listdir(self.directory):
            raise FileNotFoundError(f"A file was not created for this object.\
                \nObject full path: {self.full_path}\
                \nCreate a file using create_file method")
        with open(self.full_path, "r") as f:
            try:
                data = json.load(f)                
            except (ValueError):
                print("\nFile did not contain valid json data, contents of file set to empty dict before making changes.")
                data = {}
                
        for i in items:
            if type(i) is list:
                for j in i:
                    if j.check_type() not in data.keys():
                        data[j.check_type()] = {}    
                    data[j.check_type()][j.license] = j.__dict__
                    
            elif type(i) is Cars or type(i) is Bikes:
                if i.check_type() not in data.keys():
                    data[i.check_type()] = {}        
                              
                data[i.check_type()][i.license] = i.__dict__
        
        with open(self.full_path, "w") as f:
            json.dump(data, f, indent= 2)        
                
                    
class Vehicles(metaclass=abc.ABCMeta):
    """
    Abstract base class for vehicles.

    Attributes:
        license (str): The license plate number of the vehicle.
        make (str): The make of the vehicle.
        year (int): The year of production of the vehicle.
        mileage (int): The mileage of the vehicle.
        has_abs (bool): Indicates whether the vehicle has ABS (Anti-lock Braking System).
        price (int): The price of the vehicle.
    """
    @abc.abstractmethod
    def __init__(self, license:str, make: str, year: int, mileage: int, has_abs: bool, price: int) -> None:
        """
        Constructor method for class Vehicles
        args: 
            license (str): Has to contain 3 uppercase letters A-Z + space + 3 digits 0-9
            make (str): The make of the vehicle.
            year (int): The year of production of the vehicle.
            mileage (int): The mileage of the vehicle.
            has_abs (bool): Indicates whether the vehicle has ABS (Anti-lock Braking System).
            price (int): The price of the vehicle.
        """
        if re.match(r"[A-Z]{3} [0-9]{3}$", license):   
            self.license = license
        else:
            raise ValueError("Invalid license number. Has to contain 3 uppercase letters A-Z + space + 3 digits 0-9")  
        self.make = make
        self.year = year
        self.mileage = mileage
        self.has_abs = has_abs
        self.price = price
                
    def __str__(self) -> str:
        """
        return: a string representation of Vehicle objects and their atributes
        """
        return f"This {self.make} with license plate '{self.license}' is made in the year {self.year} and has {self.mileage} Km on board.\
        \nhas ABS: {self.has_abs}\nPrice: {self.price}"
        
    def compare(self, *compared) -> PrettyTable:
        """
        Compares the properties of a variable number of vehicles        
        args: compared (Vehicles): The vehicles to compare with
        return: A table with information of all vehicles. First row is always the main vehicle which called the method.
        """         
        result = PrettyTable()
        result.field_names = ["type", "make", "year", "mileage", "price", "license"]
        result.add_row([self.check_type(), self.make, self.year, self.mileage, self.price, self.license])
        for item in compared:
            result.add_row([item.check_type(), item.make, item.year, item.mileage, item.price, item.license])
        return result
            
    def check_type(self) -> str:
        """
        Checks the type of vehicle.
        return: The type of vehicle ('Car' or 'Bike').
        """
        if type(self) is Cars:
            return("Car")
        if type(self) is Bikes:
            return("Bike")
                         
        
class Cars(Vehicles):
    """
    represents a Bike

    Attributes:
        tires (int): The number of tires of the car.
        doors (int): The number of doors of the car.
    """
    tires = 4
    doors = 4
    
    def __init__(self, license: str, make: str, year: int, mileage: int, has_abs: bool, price: int) -> None:
        """
        inherith atributes from superclass Vehicles
        """
        super().__init__(license, make, year, mileage, has_abs, price)
        
        
    def __str__(self) -> str:
        """
        return: a string representation of Car objects and their atributes
        """
        return super().__str__() + f"\nThis car has {self.tires} tires and {self.doors} doors."
        
    def change_doors(self, new_doors: int) -> None:
        """
        change the number of doors of the car
        """
        self.doors = new_doors
        print(f"number of doors was changed to {new_doors}")
        
    def refurbish(self) -> str:
        """
        Refurbishes the car, increasing its price if it was made before 2014.

        return: A message indicating the result of the refurbishment.
        """
        if self.year < 2014:
            old_price = self.price
            self.price += 1000
            return f"Car was refurbished! Price of the vehicle has increased from {old_price} to {self.price}"
        else:
            return f"This car is made in the year {self.year}. It doesn't make much sense to refurbish it."
            
        
class Bikes(Vehicles):
    """
    Represents a bike.

    Attributes:
        tires (int): The number of tires of the bike.
        seats (int): The number of seats of the bike.
    """
    tires = 2
    seats = 2
    
    def __init__(self, license: str, make: str, year: int,
                 mileage: int, has_abs: bool, price: int) -> None:
        """
        inherith atributes from superclass Vehicles
        """
        super().__init__(license, make, year, mileage, has_abs, price)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the Bikes object.

        return: A formatted string containing information about the bike.
        """
        return super().__str__() + f"\nThis bike has {self.tires} tires and {self.seats} seats."
        
    def change_seats(self, new_seats: int) -> None:
        """
        change the value of seats on the bike
        """
        self.seats = new_seats
        print(f"number of seats was changed to {new_seats}")
        
    def add_mods(self, number_of_mods) -> str:
        """
        Adds modifications to the bike, increasing its price.
        Args:
            number_of_mods (int): The number of modifications to add.
        return: A message indicating the result of the modifications.
        """
        old_price = self.price
        for _ in range(number_of_mods):
            self.price += 800        
        return f"Bike was modded. Number of mods added: {number_of_mods}. Price of the vehicle has increased from {old_price} to {self.price}"
 

def create_random_car() -> Cars:
    """
    return: a random Cars object
    """
    makes = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Mercedes-Benz"]
        
    make = random.choice(makes)
    year = random.randint(1990, 2024)
    mileage = random.randint(0, 200000)
    has_abs = random.choice([True, False])
    price = random.randint(0, 100000)
    license = f"{"".join([random.choice(string.ascii_uppercase) for _ in range(3)])} {random.randint(100, 999)}"
    
    car = Cars(license, make, year, mileage, has_abs, price)
    return car

def create_random_bike() -> Bikes:
    """
    return: a random bike object
    """
    makes = ["Harley", "Honda", "Suzuki", "Kawasaki", "BMW"]
        
    make = random.choice(makes)
    year = random.randint(1990, 2024)
    mileage = random.randint(0, 200000)
    has_abs = random.choice([True, False])
    price = random.randint(0, 100000)
    license = f"{"".join([random.choice(string.ascii_uppercase) for _ in range(3)])} {random.randint(100, 999)}"
    
    bike = Bikes(license, make, year, mileage, has_abs, price)
    return bike

car1 = create_random_car()
print(car1)
car1.change_doors(2)
car1.refurbish()
print(car1.__dict__)

bike1 = create_random_bike()
print(bike1)
bike1.add_mods(10)
bike1.change_seats(1)
print(bike1.__dict__)

bike2 = create_random_bike()
print(bike2)
print(bike2.compare(car1, bike1))

file1 = Json_DB(path1, "test.json")
print(file1)
print(file1.__dict__)
file1.create_file()
file1.write_to_file(car1, bike1, bike2)
print(file1)

cars = [create_random_car() for _ in range(2)]
bikes = [create_random_bike() for _ in range(2)]
file1.write_to_file(car1, bike1, bikes, cars)
print(file1)