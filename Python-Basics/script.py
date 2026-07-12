"""
Python OOP Practice

Topics covered:
- Classes and objects
- Object composition
- Instance attributes and methods
- Class attributes
- Static methods
- Encapsulation
- Properties
- Abstraction
- Inheritance
- super()
- Method overriding
- Polymorphism
"""


# ============================================================
# 1. CLASSES, OBJECTS, AND OBJECT COMPOSITION
# ============================================================


class Owner:
    """Represents the owner of a dog."""

    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


class Dog:
    """Represents a dog that has an Owner object."""

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"{self.name}: Woof Woof!")


# ============================================================
# 2. INSTANCE ATTRIBUTES AND INSTANCE METHODS
# ============================================================


class Person:
    """Simple example of instance attributes and methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(
            f"Hello, my name is {self.name} "
            f"and I am {self.age} years old."
        )


# ============================================================
# 3. CLASS ATTRIBUTES
# ============================================================


class User:
    """Demonstrates class attributes shared between instances."""

    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email

        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


# ============================================================
# 4. STATIC METHODS AND INTERNAL METHODS
# ============================================================


class InterestBankAccount:
    """Demonstrates static methods and internal helper methods."""

    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(
            f"Logging {transaction_type} of ${amount}. "
            f"New balance: ${self._balance}"
        )

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


# ============================================================
# 5. BAD ENCAPSULATION EXAMPLE
# ============================================================


class BadBankAccount:
    """Demonstrates the problem with unrestricted public data."""

    def __init__(self, balance):
        self.balance = balance


# ============================================================
# 6. ENCAPSULATION AND PROPERTIES
# ============================================================


class SecureBankAccount:
    """Demonstrates controlled access to account balance."""

    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount


# ============================================================
# 7. ABSTRACTION
# ============================================================


class EmailService:
    """
    Demonstrates abstraction.

    The user only needs to call send_email().
    Internal connection details are hidden behind helper methods.
    """

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server...")

    def send_email(self):
        self._connect()
        self._authenticate()

        print("Sending email...")

        self._disconnect()


# ============================================================
# 8. INHERITANCE
# ============================================================


class Vehicle:
    """Parent class for different types of vehicles."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")


class Car(Vehicle):
    """Car inherits attributes and methods from Vehicle."""

    def __init__(
        self,
        brand,
        model,
        year,
        number_of_doors,
        number_of_wheels=4,
    ):
        super().__init__(brand, model, year)

        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    """Bike inherits attributes and methods from Vehicle."""

    def __init__(self, brand, model, year, number_of_wheels=2):
        super().__init__(brand, model, year)

        self.number_of_wheels = number_of_wheels


# ============================================================
# 9. METHOD OVERRIDING AND POLYMORPHISM
# ============================================================


class Motorcycle(Vehicle):
    """Demonstrates method overriding."""

    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print(f"{self.brand} {self.model} motorcycle engine is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} motorcycle engine is stopping.")


def inspect_vehicle(vehicle):
    """
    Demonstrates polymorphism.

    Any Vehicle-compatible object can be passed to this function.
    """

    print(
        f"Inspecting {vehicle.brand} {vehicle.model} "
        f"({type(vehicle).__name__})"
    )

    vehicle.start()
    vehicle.stop()


# ============================================================
# MAIN PROGRAM
# ============================================================


def main():
    print("\n--- 1. OBJECT COMPOSITION ---")

    owner1 = Owner(
        "Danny",
        "1234 Street, Lahore, Punjab, Pakistan",
        1234567890,
    )

    dog1 = Dog("Bruce", "German Shepherd", owner1)

    dog1.bark()

    print(dog1.owner.name)
    print(dog1.owner.address)
    print(dog1.owner.contact_number)

    owner2 = Owner(
        "Sarah",
        "5678 Road, Lahore, Punjab, Pakistan",
        9876543210,
    )

    dog2 = Dog("Max", "Labrador", owner2)

    dog2.bark()

    print(dog2.name)
    print(dog2.breed)
    print(dog2.owner.name)

    print("\n--- 2. INSTANCE METHODS ---")

    person1 = Person("Alice", 30)
    person2 = Person("Bob", 23)

    person1.greet()
    person2.greet()

    print("\n--- 3. CLASS ATTRIBUTES ---")

    user1 = User("dantheman", "dan@gmail.com")
    user2 = User("sally123", "sally@gmail.com")

    user1.display_user()
    user2.display_user()

    print(f"Total users: {User.user_count}")

    print("\n--- 4. STATIC METHODS ---")

    interest_account = InterestBankAccount("Alice", 500)

    interest_account.deposit(200)

    print(InterestBankAccount.is_valid_interest_rate(3))
    print(InterestBankAccount.is_valid_interest_rate(10))

    print("\n--- 5. BAD ENCAPSULATION ---")

    bad_account = BadBankAccount(0.0)

    bad_account.balance = -1000

    print(f"Invalid balance allowed: {bad_account.balance}")

    print("\n--- 6. ENCAPSULATION ---")

    secure_account = SecureBankAccount()

    print(f"Starting balance: ${secure_account.balance}")

    secure_account.deposit(1000)

    print(f"After deposit: ${secure_account.balance}")

    secure_account.withdraw(300)

    print(f"After withdrawal: ${secure_account.balance}")

    print("\n--- 7. ABSTRACTION ---")

    email_service = EmailService()

    email_service.send_email()

    print("\n--- 8. INHERITANCE ---")

    car = Car(
        "Ford",
        "Focus",
        2014,
        number_of_doors=5,
    )

    bike = Bike(
        "Honda",
        "Scoopy",
        2018,
    )

    print(car.__dict__)
    print(bike.__dict__)

    car.start()
    bike.start()

    print("\n--- 9. POLYMORPHISM ---")

    vehicles = [
        Car("Ford", "Focus", 2008, number_of_doors=5),
        Bike("Honda", "Scoopy", 2018),
        Motorcycle("Yamaha", "R1", 2024),
    ]

    for vehicle in vehicles:
        inspect_vehicle(vehicle)


if __name__ == "__main__":
    main()
  
  
  
  
  
  
  
  
                   