import unittest
from manual_test import JoystickHandler

class TestManualTest(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual("foo".upper(), "FOO")

    # def test_isupper(self):
    #     self.assertTrue("FOO".isupper())
    #     self.assertFalse("Foo".isupper())

    # def test_split(self):
    #     s = "hello world"
    #     self.assertEqual(s.split(), ["hello", "world"])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_axis_signal(self):
        stick = JoystickHandler(None)

        self.assertEquals(stick.axis_to_signal_format(0),65536/2)
        self.assertEquals(stick.axis_to_signal_format(1),65536)
    


if __name__ == "__main__":
    unittest.main()
