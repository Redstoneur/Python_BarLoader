import unittest
from Bar_Loader.BarLoaderExpert import BarLoaderExpert, IterativeBarLoaderExpert, UniqueProcessBarLoaderExpert
from time import sleep, time

class TestBarLoaderExpert(unittest.TestCase):
    def setUp(self):
        self.bar = BarLoaderExpert(total=100, task_name="LoadingExpert", enable_value=True)

    def test_start_initializes_correctly(self):
        self.bar.start()
        self.assertEqual(self.bar.nb, 0)

    def test_next_increments_correctly(self):
        self.bar.start()
        self.bar.next()
        self.assertEqual(self.bar.nb, 1)

    def test_end_finalizes_correctly(self):
        self.bar.start()
        for _ in range(100):
            self.bar.next()
        self.bar.end()
        self.assertEqual(self.bar.nb, 100)

    def test_end_force_finalizes_correctly(self):
        self.bar.start()
        self.bar.end(force=True)
        self.assertEqual(self.bar.nb, 100)

class TestIterativeBarLoaderExpert(unittest.TestCase):
    def setUp(self):
        self.bar = IterativeBarLoaderExpert(total=100, task_name="LoadingExpert")

    def test_start_initializes_correctly(self):
        self.bar.start()
        self.assertEqual(self.bar.nb, 0)

    def test_next_increments_correctly(self):
        self.bar.start()
        self.bar.next()
        self.assertEqual(self.bar.nb, 1)

    def test_end_finalizes_correctly(self):
        self.bar.start()
        for _ in range(100):
            self.bar.next()
        self.bar.end()
        self.assertEqual(self.bar.nb, 100)

class TestUniqueProcessBarLoaderExpert(unittest.TestCase):
    def setUp(self):
        self.bar = UniqueProcessBarLoaderExpert(total=100, task_name="LoadingExpert")

    def test_start_initializes_correctly(self):
        self.bar.start()
        self.assertEqual(self.bar.nb, 0)

    def test_end_finalizes_correctly(self):
        self.bar.start()
        self.bar.end()
        self.assertEqual(self.bar.nb, 100)

if __name__ == '__main__':
    unittest.main()