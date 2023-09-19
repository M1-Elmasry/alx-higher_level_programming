import unittest
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
from io import StringIO


class TestSquare(unittest.TestCase):
    def test_module_docs(self):
        module_name = Square.__module__
        module_doc = module_name.__doc__
        if module_doc is None:
            module_doc = ""
        self.assertTrue(len(module_doc) >= 1)

    def test_Base_class_docs(self):
        cls_doc = Square.__doc__
        if cls_doc is None:
            cls_doc = ""
        self.assertTrue(len(cls_doc) >= 1)

    def test_Square_instance(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_Square_without_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_Square_invalid_size(self):
        with self.assertRaises(ValueError):
            Square(-2)

    def test_Square_invalid_size2(self):
        with self.assertRaises(TypeError):
            Square("W")

    def test_Square_get_size_and_x(self):
        r = Square(10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 0)
        r = Square(10, 20, 5, 10)
        self.assertEqual(r.x, 20)

    def test_Square_get_size_and_y(self):
        r = Square(10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.y, 0)
        r = Square(10, 20, 5, 10)
        self.assertEqual(r.y, 5)

    def test_Square_set_size_valid(self):
        r = Square(10)
        r.size = 15
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 15)

    def test_Square_set_size_invalid(self):
        r = Square(10)
        with self.assertRaises(ValueError):
            r.size = -5

    def test_Square_set_x_valid(self):
        r = Square(10)
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_Square_set_x_invalid(self):
        r = Square(10)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_Square_set_y_valid(self):
        r = Square(10)
        r.y = 15
        self.assertEqual(r.y, 15)

    def test_Square_set_y_invalid(self):
        r = Square(10)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_Square_id(self):
        r = Square(24, 1, 1, 10)
        self.assertEqual(r.id, 10)

    def test_Square_area_doc(self):
        r = Square(1)
        r_doc = r.area.__doc__ if r.area.__doc__ is not None else ""
        self.assertTrue(len(r_doc) >= 1)

    def test_Square_area(self):
        r = Square(5)
        self.assertEqual(r.area(), 25)
        r = Square(10)
        self.assertEqual(r.area(), 100)
        r = Square(500)
        self.assertEqual(r.area(), 250000)

    def test_Square_display_doc(self):
        r = Square(1)
        r_doc = r.display.__doc__ if r.display.__doc__ is not None else ""
        self.assertTrue(len(r_doc) >= 1)

    def test_Square_display(self):
        r = Square(4)
        file = StringIO()
        with redirect_stdout(file):
            r.display()
            output = file.getvalue()
            self.assertEqual(output, "####\n####\n####\n####\n")

    def test_Square_display_x_y(self):
        r = Square(4, 1, 2)
        file = StringIO()
        with redirect_stdout(file):
            r.display()
            output = file.getvalue()
            self.assertEqual(output, "\n\n ####\n ####\n ####\n ####\n")

    def test_Square_str(self):
        r = Square(10)
        self.assertEqual(str(r), f"[Square] ({r.id}) 0/0 - 10")
        r = Square(30, 10, 7, 1695)
        self.assertEqual(str(r), "[Square] (1695) 10/7 - 30")

    def test_Square_update(self):
        r = Square(10)
        r.update(235, 15, 30, 15)
        self.assertEqual(r.id, 235)
        self.assertEqual(r.size, 15)
        self.assertEqual(r.x, 30)
        self.assertTrue(r.y, 15)

        r.update(id=198, x=20, size=15)
        self.assertEqual(r.id, 198)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.size, 15)

        r.update(1024, x=15)
        self.assertEqual(r.id, 1024)
        # x will not update becuase *args exists
        self.assertTrue(r.x, 20)

    def test_update_raise(self):
        r = Square(10)
        with self.assertRaises(ValueError):
            r.update(123, -15, 20)
