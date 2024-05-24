import random
import unittest
from unittest import TestCase

from choices import Choices


class ChoicesTestOps(TestCase):

    @classmethod
    def setUpClass(cls):
        gen = random.Random()

    def test_empty_input(self):
        c = Choices([], [])
        self.assertRaises(IndexError, c.choice)

    def test_single_element_input(self):
        p = [50]
        c = Choices(p)
        self.assertEqual(p[0], c.choice())

    def test_with_two_elements_no_weights(self):
        p, n = [10, 20], 1000
        p_size = len(p)
        choices = Choices(p)
        generated_seq = [choices.choice() for _ in range(n)]
        seq_weights = [generated_seq.count(p[i])/n for i in range(p_size)]
        threshold = 0.025
        self.assertTrue(all(abs(seq_weights[i] - choices.weights_norm[i]) <= threshold for i in range(p_size)))


if __name__ == "__main__":
    unittest.main()




