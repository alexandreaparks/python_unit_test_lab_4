from unittest import TestCase
import area


class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        # height 4 and base 5 should have area 10
        self.assertEqual(10, area.triangle_area(4, 5))

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    # test to check if an exception is raised using a context manager
    # test fails if specified error is NOT raised, or if a different error is raised
    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-3, 0)

        with self.assertRaises(ValueError):
            area.triangle_area(0, -3)

        with self.assertRaises(ValueError):
            area.triangle_area(-3, -3)

    def test_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 4))
        self.assertEqual(0, area.triangle_area(4, 0))
        self.assertEqual(0, area.triangle_area(0, 0))
