import numpy

from data_utils import *


class k_means:

    def __init__(self, num_iterations=200, num_class=3):
        self.k = num_class
        self.num_iterations = num_iterations

    def train(self, data):
        pass

    def predict(self, data):
        pass

data, labels = read_iris_data()
model = k_means()

