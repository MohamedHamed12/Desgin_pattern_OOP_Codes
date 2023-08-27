
# bad code
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False
a = ParkingSystem(1, 1, 0)
print(a.addCar(1))




# Utilizing Design Patterns:
#   Factory Pattern , Composition Pattern
# 
# Adhering to Software Design Principles:
# Single Responsibility Principle , Open-Closed Principle
#
# Leveraging Enum Pattern

from enum import Enum

class CarType(Enum):
    Big = 1
    Medium = 2
    Small = 3


class ParkingSpot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.available_spots = capacity

    def park(self) -> bool:
        """
            Function to park a vehicle.
            Returns:
                bool: True if the `e vehicle is successfully parked, False otherwise.
        """
        # Check if there are available parking spots
        if self.available_spots > 0:
            # Decrement the available spots count
            self.available_spots -= 1
            return True
        else:
            return False


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spots = {
            CarType.Big: ParkingSpot(big),
            CarType.Medium: ParkingSpot(medium),
            CarType.Small: ParkingSpot(small),
        }

    def addCar(self, carType: int) -> bool:
        """
            Adds a car of a given type to the parking lot.
            Args:
                carType (int): The type of the car to be added.
            Returns:
                bool: True if the car is added successfully, False otherwise.
        """
        if carType in self.spots:
            return self.spots[carType].park()
        return False
    def addSpot(self, capacity: int):
        """
            Adds a parking spot.
            Args:
                capacity (int): The capacity of the parking spot.
        """
        self.spots[CarType.Big] = ParkingSpot(capacity)


