# import math


def circle_area(radius):
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not numeric input')
    if radius <= 0:
        raise ValueError('Not positive')
    return (radius ** 2) * 3.14159       # (math.pow(radius, 2)) * math.pi


def rectangle_area(length, width):
    if type(length) != int and type(length) != float:
        raise TypeError('Not numeric input')
    if type(width) != int and type(width) != float:
        raise TypeError('Not numeric input')
    if length <= 0 or width <= 0:
        raise ValueError('Not positive')
    return length * width


def square_area(length):
    if type(length) != int and type(length) != float:
        raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    return length ** 2      # math.pow(length, 2)


def triangle_area(base, height):
    if type(base) != int and type(base) != float:
        raise TypeError('Not numeric input')
    if type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')
    if base <= 0 or height <= 0:
        raise ValueError('Not positive')
    return (base * height) / 2
