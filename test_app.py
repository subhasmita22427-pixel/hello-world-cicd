import unittest
from app import hello_world, welcome_message


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")

    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message_subhasmita(self):
        self.assertEqual(
            welcome_message("Subhasmita"),
            "Welcome to DevOps, Subhasmita!"
        )

    def test_welcome_message_vansh(self):
        self.assertEqual(
            welcome_message("Vansh"),
            "Welcome to DevOps, Vansh!"
        )


if __name__ == "__main__":
    unittest.main()
