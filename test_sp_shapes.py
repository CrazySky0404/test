import unittest
from shapes_functions import get_circle_perimeter_area, get_square_perimeter_area, get_rect_perimeter_area_side, \
    get_rect_perimeter_area_co


class ShapesTestCase(unittest.TestCase):
    """Tests for 'shapes_functions.py'."""
    def test_correct_circle_ps(self):
        output = get_circle_perimeter_area(3)
        self.assertEqual(output, f'Circle: Perimeter 18, Area 28')

    def test_correct_square_ps(self):
        output = get_square_perimeter_area(4)
        self.assertEqual(output, f'Square: Perimeter 16, Area 16')

    def test_correct_rectangle_ps_side(self):
        output = get_rect_perimeter_area_side([2], [3])
        self.assertEqual(output, f'Rectangle: Perimeter 10, Area 6')

    def test_correct_rect_ps_side(self):
        output = get_rect_perimeter_area_co([2,3], [3,4])
        self.assertEqual(output, f'Rectangle: Perimeter 4, Area 1')


if __name__=='__main__':
    unittest.main()