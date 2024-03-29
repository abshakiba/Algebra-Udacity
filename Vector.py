from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 45

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalized the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError;
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.length = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitute(self):
        magnitute = [x ** 2 for x in self.coordinates]
        return Decimal(sqrt(sum(magnitute)))

    def normalized(self):
        try:
            return self.times_scalar(Decimal('1.0')/self.magnitute())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees = False):
        try:
            angle_in_radians = acos(self.normalized().dot(v.normalized()))
            if in_degrees:
                return angle_in_radians*180./pi
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute angle with the zero vector!")
            else:
                raise e

print(Vector([7.887,4.138]).dot(Vector([-8.802,6.776])))
print(Vector([-5.955,-4.904,-1.874]).dot(Vector([-4.496,-8.755,7.103])))
print(Vector([3.183, -7.627]).angle_with(Vector([-2.668,5.319])))
print(Vector([7.35,0.221,5.188]).angle_with(Vector([2.751,8.259,3.985]), True))
