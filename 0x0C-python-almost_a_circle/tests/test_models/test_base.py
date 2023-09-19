import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_module_docs(self):
        module_name = Base.__module__
        module_doc = module_name.__doc__
        if module_doc is None:
            module_doc = ""
        self.assertTrue(len(module_doc) >= 1)

    def test_Base_class_docs(self):
        cls_doc = Base.__doc__
        if cls_doc is None:
            cls_doc = ""
        self.assertTrue(len(cls_doc) >= 1)

    def test_Base_with_id_value(self):
        a = Base(10)
        b = Base()
        c = Base()
        d = Base(15)
        e = Base()
        self.assertEqual(a.id, 10)
        self.assertEqual(b.id, 1)
        self.assertEqual(c.id, 2)
        self.assertEqual(d.id, 15)
        self.assertEqual(e.id, 3)
