# CPE 202 Lab 1
import math
from math import *


# represents a location using name, latitude and longitude
class Location:
    def __init__(self, name: str, lat: float, lon: float) -> None:
        self.name = name  # string for name of location
        self.lat = lat  # latitude in degrees (float)
        self.lon = lon  # longitude in degrees (float)

    # ADD BOILERPLATE HERE (__eq__ and __repr__ functions)
    def __eq__(self, other) -> bool:
        return type(other) is type(self) and other.name == self.name and math.isclose(
                other.lat, self.lat) and math.isclose(other.lon, self.lon)

    def __repr__(self) -> str:
        return "Location('{}', {}, {})".format(self.name, self.lat, self.lon)


# 100% Code coverage NOT required due to the main function
def main() -> None:
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:", loc1)
    print("Location 2:", loc2)
    print("Location 3:", loc3)
    print("Location 4:", loc4)

    print("\nLocation 1 equals Location 2:", loc1 == loc2)
    print("Location 1 equals Location 3:", loc1 == loc3)
    print("Location 1 equals Location 4:", loc1 == loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)


if __name__ == "__main__":
    main()
