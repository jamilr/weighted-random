import collections
import math
import random
from bisect import bisect
from collections import defaultdict

import numpy as np
import random as r


class Choices(object):

    def __init__(self, population: np.array, weights=None):
        self._population = np.array(population)
        self._weights = np.array(weights)
        self._weights_norm = None
        self._weights_cum_sum = None
        self._r = r.Random()

    def _normalize_weights(self):
        if self._is_empty(self._population):
            raise IndexError
        return self._weights/self._weights.sum() if not self._is_empty(self._weights) and self._weights.shape == self._population.shape else self._uniform_weights()

    def _uniform_weights(self):
        if self._is_empty(self._population):
            raise IndexError
        population_size = len(self._population)
        return np.array([1/population_size]*population_size)

    @property
    def weights(self):
        return self._weights

    @property
    def weights_norm(self):
        return self._weights_norm

    def choice(self):
        if self._is_empty(self._population):
            raise IndexError
        if self._weights_norm is None:
            if self._is_empty(self._weights):
                self._weights_norm = self._uniform_weights()
            else:
                self._weights_norm = self._normalize_weights()
            self._weights_cum_sum = np.cumsum(self._weights_norm)
        return self._population[np.searchsorted(self._weights_cum_sum, self._r.random())]

    def _is_empty(self, inp: np.array):
        return not(inp.ndim and inp.size)


if __name__ == '__main__':
    p = [1,2,3,4,5]
    w = [10, 10, 60, 10, 10]
    N = 10000
    c = Choices(p, w)
    calibrated_weights = [0]*len(w)
    seq = [c.choice() for i in range(N)]
    frqs = collections.Counter(seq)
    for idx, num in enumerate(p):
        calibrated_weights[idx] = round(frqs[num]/N, 2)

    calib_errors = [round(abs(exp_w - calib_w), 2) for exp_w, calib_w in zip(c.weights_norm, calibrated_weights)]
    threshold = 0.03

    print(f'Expected Weights: {c.weights_norm}')
    print(f'Calibrated Weights: {calibrated_weights}')
    print(f'Exp-Calib Weights Diff: {[round(abs(exp_w-calib_w), 2) for exp_w, calib_w in zip(c.weights_norm, calibrated_weights)]}')
    print(f'Converges: {all(err < threshold for err in calib_errors)}')












