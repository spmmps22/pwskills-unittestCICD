import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    
    def test_say_hello(self):
        g = Greeter("Siddharth")
        self.assertEqual(g.say_hello(),"Hello, Gagan!")


if __name__ == "__main__":
    unittest.main()