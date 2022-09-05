
from shapes_functions import get_circle_perimeter_area, get_square_perimeter_area, read_square, read_circle, read_rect, \
    get_rect_perimetr_area

figurs = {'square': {'number': 1, 'read': read_square, 'calculate': get_square_perimeter_area},
          'rectangle': {'number': 2, 'read': read_rect, 'calculate': get_rect_perimetr_area},
          'circle': {'number': 3, 'read': read_circle, 'calculate': get_circle_perimeter_area}}

try:

    while True:
        prompt = 'Choose the geometric shape and calculate its area and perimeter:\n'
        for name, figur in figurs.items():
            prompt += f'- if it is a {name}, then press {figur["number"]} \n'
        prompt += f'Number your shape is: '
        question = int(input(prompt))

        while True:
            figur_found = False
            for figur in figurs.values():
                if question == figur['number']:
                    *date, = figur['read']()
                    output = figur['calculate'](*date)
                    print(output)
                    figur_found = True
                    break
            if figur_found:
                break
            else:
                print('Please, enter 1, 2 or 3.')
                question = int(input('Number your shape is: '))

        answer = input("Do you want to calculate another shape? y/n  ")
        if answer == 'y':
            pass
        else:
            print("Buy!")
            break

except ValueError:
    print('Please, enter a number.')
except Exception as err:
    print('Some other error occured.', str(err))



