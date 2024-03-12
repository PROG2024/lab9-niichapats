"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
import math

from circle import Circle


class CircleTest(unittest.TestCase):
    def test_add_area(self):
        circle1 = Circle(3)
        circle2 = Circle(4)
        circle3 = circle1.add_area(circle2)
        expected_radius = math.hypot(circle1.get_radius(), circle2.get_radius())
        self.assertEqual(circle3.get_radius(), expected_radius)
        self.assertEqual(circle3.get_area(), math.pi*expected_radius**2)

    def test_add_area_one_zero(self):
        circle1 = Circle(3)
        circle2 = Circle(0)
        circle3 = circle1.add_area(circle2)
        self.assertEqual(circle3.get_radius(), circle1.radius)
        self.assertEqual(circle3.get_area(), circle1.get_area())

    def test_construct_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)
