import unittest

from Bar_Loader.BarLoader import BarLoader, IterativeBarLoader, UniqueProcessBarLoader


class TestBarLoader(unittest.TestCase):
    def setUp(self):
        self.bar = BarLoader(total=100, task_name="Loading", enable_value=True)

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


class TestIterativeBarLoader(unittest.TestCase):
    def setUp(self):
        self.bar = IterativeBarLoader(total=100, task_name="Loading")

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


class TestUniqueProcessBarLoader(unittest.TestCase):
    def setUp(self):
        self.bar = UniqueProcessBarLoader(total=100, task_name="Loading")

    def test_start_initializes_correctly(self):
        self.bar.start()
        self.assertEqual(self.bar.nb, 0)

    def test_end_force_finalizes_correctly(self):
        self.bar.start()
        self.bar.end()
        self.assertEqual(self.bar.nb, 100)


if __name__ == '__main__':
    unittest.main()
