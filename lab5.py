import math


# Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle,
# Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.

class Shape:
    def area(self) -> int:
        pass

    def perimeter(self) -> int:
        pass


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> int:
        return self.a + self.b + self.c


circle = Circle(10)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

rectangle = Rectangle(2, 3)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

triangle = Triangle(3, 4, 5)
print(f"Triangle Area: {triangle.area()}")
print(f"Triangle Perimeter: {triangle.perimeter()}")


# Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. Implement
# methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number: int, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def interest(self) -> float:
        pass


class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: int = 0, interest_rate: float = 0.05) -> None:
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: int = 0, overdraft_limit: int = 1000) -> None:
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")


savings_account = SavingsAccount(123456, 1000, 0.03)
savings_account.deposit(500)
savings_account.interest()
savings_account.withdraw(200)

checking_account = CheckingAccount(123457, 500, 100)
checking_account.deposit(200)
checking_account.withdraw(700)


# Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific
# types of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the
# vehicle type.

class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, fuel_efficiency: int) -> None:
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # kms per liters of gas

    def calculate_mileage(self, distance: float) -> float:
        return distance / self.fuel_efficiency


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, owner: str) -> None:
        super().__init__(make, model, year)
        self.owner = owner

    def display_owner(self) -> None:
        print(f"Motorcycle {self.make}, {self.model}, {self.year} has the owner: {self.owner}")


class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, towing_capacity: int) -> None:
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self) -> int:
        return self.towing_capacity


car = Car("Toyota", "Camry", 2022, 30)
mileage = car.calculate_mileage(150)
print(f"Mileage: {mileage:.2f} miles")

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, "meow")
motorcycle.display_owner()

truck = Truck("Ford", "F-150", 2022, 10000)
towing_capacity = truck.calculate_towing_capacity()
print(f"Towing Capacity: {towing_capacity} pounds")


# Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like
# Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their
# roles.

class Employee:
    def __init__(self, name: str, employee_id: str) -> None:
        self.name = name
        self.employee_id = employee_id

    def display_info(self) -> None:
        print(f"Employee ID: {self.employee_id}\nName: {self.name}")


class Manager(Employee):
    def __init__(self, name: str, employee_id: str, salary: int, department: str) -> None:
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self) -> None:
        super().display_info()
        print(f"Position: Manager\nSalary: ${self.salary}\nDepartment: {self.department}")

    def conduct_meeting(self) -> None:
        print(f"{self.name} is conducting a meeting.")


class Engineer(Employee):
    def __init__(self, name: str, employee_id: str, salary: int, programming_language: str) -> None:
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self) -> None:
        super().display_info()
        print(f"Position: Engineer\nSalary: ${self.salary}\nProgramming Language: {self.programming_language}")

    def write_code(self) -> None:
        print(f"{self.name} is playing The Sims instead of working.")


class Salesperson(Employee):
    def __init__(self, name: str, employee_id: str, salary: int, territory: str) -> None:
        super().__init__(name, employee_id)
        self.salary = salary
        self.territory = territory

    def display_info(self) -> None:
        super().display_info()
        print(f"Position: Salesperson\nSalary: ${self.salary}\nTerritory: {self.territory}")

    def make_sale(self) -> None:
        print(f"{self.name} sold a perfume sample.")


manager = Manager("John Smith", "M001", 80000, "Marketing")
manager.display_info()
manager.conduct_meeting()

engineer = Engineer("Alice Johnson", "E001", 70000, "Java")
engineer.display_info()
engineer.write_code()

salesperson = Salesperson("Bob Miller", "S001", 60000, "Heaven")
salesperson.display_info()
salesperson.make_sale()


# Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird,
# and Fish. Add properties and methods to represent characteristics unique to each animal group.
class Animal:
    def __init__(self, name: str, habitat: str) -> None:
        self.name = name
        self.habitat = habitat

    def display_info(self) -> None:
        print(f"Name: {self.name}\nHabitat: {self.habitat}")


class Mammal(Animal):
    def __init__(self, name: str, habitat: str, fur_color: str):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def display_info(self):
        super().display_info()
        print(f"Class: Mammal\nFur Color: {self.fur_color}")

    def give_birth(self):
        print(f"{self.name} is giving birth.")


class Bird(Animal):
    def __init__(self, name: str, habitat: str, feather_color) -> None:
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def display_info(self) -> None:
        super().display_info()
        print(f"Class: Bird\nFeather color: {self.feather_color}")

    def build_nest(self) -> None:
        print(f"{self.name} is flying high in the sky.")


class Fish(Animal):
    def __init__(self, name: str, habitat: str, fin_type: str) -> None:
        super().__init__(name, habitat)
        self.fin_type = fin_type

    def display_info(self) -> None:
        super().display_info()
        print(f"Class: Fish\nFin Type: {self.fin_type}")

    def lay_eggs(self) -> None:
        print(f"{self.name} is swimming in the ocean. Bloop Bloop.")


lion = Mammal("Lion", "Grasslands", "Golden")
lion.display_info()
lion.give_birth()

eagle = Bird("Eagle", "Mountains", "Grey")
eagle.display_info()
eagle.build_nest()

shark = Fish("Great White Shark", "Oceans", "Dorsal")
shark.display_info()
shark.lay_eggs()


# Design a library catalog system with a base class LibraryItem and subclasses for different types of items like
# Book, DVD, and Magazine. Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self, title: str, call_number: str, available=True) -> None:
        self.title = title
        self.call_number = call_number
        self.available = available

    def display_info(self) -> None:
        print(f"Title: {self.title}\nCall Number: {self.call_number}\nAvailable: {'Yes' if self.available else 'No'}")

    def check_out(self) -> None:
        if self.available:
            print(f"{self.title} checked out successfully.")
            self.available = False
        else:
            print(f"{self.title} is not available for checkout.")

    def return_item(self) -> None:
        if not self.available:
            print(f"{self.title} returned successfully.")
            self.available = True
        else:
            print(f"{self.title} is already available.")


class Book(LibraryItem):
    def __init__(self, title: str, call_number: str, author: str, num_pages: int, available: bool = True) -> None:
        super().__init__(title, call_number, available)
        self.author = author
        self.num_pages = num_pages

    def display_info(self) -> None:
        super().display_info()
        print(f"Author: {self.author}\nNumber of Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title: str, call_number: str, director: str, running_time: int, available: bool = True) -> None:
        super().__init__(title, call_number, available)
        self.director = director
        self.running_time = running_time

    def display_info(self) -> None:
        super().display_info()
        print(f"Director: {self.director}\nRunning Time: {self.running_time} minutes")


class Magazine(LibraryItem):
    def __init__(self, title: str, call_number: str, issue_date: str, available: bool = True) -> None:
        super().__init__(title, call_number, available)
        self.issue_date = issue_date

    def display_info(self) -> None:
        super().display_info()
        print(f"Issue Date: {self.issue_date}")


book = Book("The Catcher in the Rye", "B001", "J.D. Salinger", 224)
book.display_info()
book.check_out()
book.return_item()

dvd = DVD("Inception", "D001", "Christopher Nolan", 148)
dvd.display_info()
dvd.check_out()
dvd.check_out()  # Trying to check out an already checked-out item
dvd.return_item()

magazine = Magazine("National Geographic", "M001", "January 2023")
magazine.display_info()
magazine.return_item()
