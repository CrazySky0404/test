import math


def read_circle():
    radius = int(input("Enter Radius of circle: "))
    return radius,


def read_square():
    side = int(input("Enter side of square: "))
    return side,


def read_rect():
    ab_list = input("Enter first side or BottomLeft of rectangle: ").split()
    if len(ab_list) == 1:
        cd_list = input("Enter second side of rectangle: ").split()
    else:
        cd_list = input("Enter TopRight of rectangle: ").split()
    return ab_list, cd_list


def get_rect_perimetr_area(ab_list,cd_list):
    if len(ab_list) == 1:
        output = get_rect_perimeter_area_side(ab_list, cd_list)
    else:
        output = get_rect_perimeter_area_co(ab_list, cd_list)
    return output


def get_circle_perimeter_area(radius):
    circle_perimeter = int(2 * math.pi * radius)
    circle_area = int(math.pi * radius**2)
    return f'Circle: Perimeter {circle_perimeter}, Area {circle_area}'


def get_square_perimeter_area(side):
    square_perimeter = 4 * side
    square_area = side ** 2
    return f'Square: Perimeter {square_perimeter}, Area {square_area}'


def get_rect_perimeter_area_side(ab_list, cd_list):
    rectangle_perimeter = 2 * (int(ab_list[0]) + int(cd_list[0]))
    rectangle_area = int(ab_list[0]) * int(cd_list[0])
    return f'Rectangle: Perimeter {rectangle_perimeter}, Area {rectangle_area}'


def get_rect_perimeter_area_co(ab_list, cd_list):
    rectangle_perimeter = 2 * (abs(int(cd_list[0]) - int(ab_list[0])) + abs(int(cd_list[1]) - int(ab_list[1])))
    rectangle_area = abs(int(cd_list[0]) - int(ab_list[0])) * abs(int(cd_list[1]) - int(ab_list[1]))
    return f'Rectangle: Perimeter {rectangle_perimeter}, Area {rectangle_area}'