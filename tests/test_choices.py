import pytest
from _pytest.python_api import approx

from choices import Choices


class TestChoices:

    @pytest.fixture
    def empty_input(self):
        return [], []

    def test_empty_input(self, empty_input):
        population, weights = empty_input
        with pytest.raises(IndexError):
            Choices(population, weights).choice()

    def test_single_element_input(self):
        p = [50]
        c = Choices(p)
        assert c.choice() == p[0]

    def test_with_two_elements_no_weights(self):
        population, n = [10, 20], 1000
        p_size = len(population)
        choices = Choices(population)
        generated_seq = [choices.choice() for _ in range(n)]
        seq_weights = [generated_seq.count(population[i])/n for i in range(p_size)]
        threshold = 0.025
        (all(abs(seq_weights[i] - choices.weights_norm[i]) == approx(threshold) for i in range(p_size)))





