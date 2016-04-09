#!/usr/bin/env python3

import unittest
import sys

import autoenum


class AutoEnumTestCase(unittest.TestCase):
    def test_valid_with_tuple(self):
        class Color(autoenum.AutoEnum):
            red = ()
            green = ()
            blue = ()

        self.assertIs(Color.red, Color.red)
        self.assertEqual(Color.red, Color.red)
        self.assertIsNot(Color.red, Color.green)
        self.assertNotEqual(Color.red, Color.green)
        self.assertIsNot(Color.green, Color.blue)

        self.assertIsInstance(Color.red, Color)

        if sys.version_info >= (3, 4):  # pragma: no cover
            self.assertEqual(Color.red.value, 1)
            self.assertEqual(Color.green.value, 2)
            self.assertEqual(Color.blue.value, 3)
        else:
            # enum34 behaves non-deterministically, and thus, member
            # values cannot be predicted.
            pass

        self.assertEqual(Color.red.name, 'red')
        self.assertEqual(Color.green.name, 'green')
        self.assertEqual(Color.blue.name, 'blue')

        class Shape(autoenum.AutoEnum):
            circle = ()
            triangle = ()
            square = ()

        self.assertIsNot(Color.red, Shape.circle)
        self.assertNotEqual(Color.red, Shape.circle)

    def test_invalid_key_reuse(self):
        # This is allowed in Python 2.
        if sys.version_info >= (3, 0):  # pragma: no cover
            with self.assertRaises(TypeError):
                class Color(autoenum.AutoEnum):
                    red = ()
                    red = ()

    def test_restricted_subclassing(self):
        class Color(autoenum.AutoEnum):
            red = ()
            green = ()
            blue = ()

        with self.assertRaises(TypeError):
            class MoreColor(Color):
                pink = ()
