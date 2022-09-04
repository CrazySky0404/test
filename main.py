
from shapes_functions import get_circle_perimeter_area, get_square_perimeter_area, get_rect_perimeter_area_side, \
    get_rect_perimeter_area_co

try:

    while True:
        question = int(input('Choose the geometric shape and calculate its area and perimeter:\n'
                             '- if it is a square, then press 1 \n'
                             '- if it is a rectangle, then press 2 \n'
                             '- if it is a circle, then press 3\n'
                             'Number your shape is: '))
        while True:
            if question == 1:

                side = int(input("Enter side of square: "))
                output = get_square_perimeter_area(side)
                print(output)
                break

            elif question == 2:
                ab_list = input("Enter first side or BottomLeft of rectangle: ").split()
                if len(ab_list) == 1:
                    cd_list = input("Enter second side of rectangle: ").split()
                    output = get_rect_perimeter_area_side(ab_list, cd_list)
                    print(output)
                    break
                else:
                    cd_list = input("Enter TopRight of rectangle: ").split()
                    output = get_rect_perimeter_area_co(ab_list, cd_list)
                    print(output)
                    break

            elif question == 3:
                radius = int(input("Enter Radius of circle: "))
                output = get_circle_perimeter_area(radius)
                print(output)
                break
            else:
                print('Please, enter 1, 2 or 3.')
                question = int(input('Number your shape is: '))

        answer = input("Do you want to calculate another shape? y/n ")
        if answer == 'y':
            pass
        else:
            print("Buy!")
            break

except ValueError:
    print('Please, enter a number.')
except Exception as err:
    print('Some other error occured.', str(err))



