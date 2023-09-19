import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout
from io import StringIO


class TestRectangle(unittest.TestCase):
    def test_module_docs(self):
        module_name = Rectangle.__module__
        module_doc = module_name.__doc__
        if module_doc is None:
            module_doc = ""
        self.assertTrue(len(module_doc) >= 1)

    def test_Base_class_docs(self):
        cls_doc = Rectangle.__doc__
        if cls_doc is None:
            cls_doc = ""
        self.assertTrue(len(cls_doc) >= 1)

    def test_Rectangle_instance(self):
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_Rectangle_without_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_Rectangle_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)

    def test_Rectangle_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -20)

    def test_Rectangle_invalid_width2(self):
        with self.assertRaises(TypeError):
            Rectangle("W", 4)

    def test_Rectangle_invalid_height2(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "H")

    def test_Rectangle_get_width_and_x(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.x, 0)
        r = Rectangle(10, 20, 5, 10)
        self.assertEqual(r.x, 5)

    def test_Rectangle_get_height_and_y(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.y, 0)
        r = Rectangle(10, 20, 5, 10)
        self.assertEqual(r.y, 10)

    def test_Rectangle_set_width_valid(self):
        r = Rectangle(10, 20)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_Rectangle_set_width_invalid(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_Rectangle_set_height_valid(self):
        r = Rectangle(10, 20)
        r.height = 15
        self.assertEqual(r.height, 15)

    def test_Rectangle_set_height_invalid(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_Rectangle_set_x_valid(self):
        r = Rectangle(10, 20)
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_Rectangle_set_x_invalid(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_Rectangle_set_y_valid(self):
        r = Rectangle(10, 20)
        r.y = 15
        self.assertEqual(r.y, 15)

    def test_Rectangle_set_y_invalid(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_Rectangle_id(self):
        r = Rectangle(12, 24, 1, 1, 10)
        self.assertEqual(r.id, 10)

    def test_Rectangle_area_doc(self):
        r = Rectangle(1, 2)
        r_doc = r.area.__doc__ if r.area.__doc__ is not None else ""
        self.assertTrue(len(r_doc) >= 1)

    def test_Rectangle_area(self):
        r = Rectangle(5, 7)
        self.assertEqual(r.area(), 35)
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)
        r = Rectangle(500, 1000)
        self.assertEqual(r.area(), 500000)

    def test_Rectangle_display_doc(self):
        r = Rectangle(1, 2)
        r_doc = r.display.__doc__ if r.display.__doc__ is not None else ""
        self.assertTrue(len(r_doc) >= 1)

    def test_Rectangle_display(self):
        r = Rectangle(4, 4)
        file = StringIO()
        with redirect_stdout(file):
            r.display()
            output = file.getvalue()
            self.assertEqual(output, "####\n####\n####\n####\n")

    def test_Rectangle_display_x_y(self):
        r = Rectangle(4, 4, 1, 2)
        file = StringIO()
        with redirect_stdout(file):
            r.display()
            output = file.getvalue()
            self.assertEqual(output, "\n\n ####\n ####\n ####\n ####\n")

    def test_Rectangle_str(self):
        r = Rectangle(10, 20)
        r_id = r.id
        self.assertEqual(str(r), f"[Rectangle] ({r_id}) 0/0 - 10/20")
        r = Rectangle(15, 30, 10, 7, 1695)
        self.assertEqual(str(r), "[Rectangle] (1695) 10/7 - 15/30")

    def test_Rectangle_update(self):
        r = Rectangle(10, 20)
        r.update(235, 15, 30)
        self.assertEqual(r.id, 235)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 30)

        r.update(1024, 256, 512, 8, 16)
        self.assertEqual(r.id, 1024)
        self.assertEqual(r.width, 256)
        self.assertEqual(r.height, 512)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 16)

        r.update(id=198, x=20, height=15)
        self.assertEqual(r.id, 198)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.height, 15)

        r.update(1024, x=15)
        self.assertEqual(r.id, 1024)
        # x will not update becuase *args exists
        self.assertTrue(r.x, 20)

    def test_update_raise(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.update(123, -15, 20)
