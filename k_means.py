import numpy as np
import random

from data_utils import *


class k_means:
    def __init__(self, num_iterations=20, k=3):
        self.k = k
        self.num_iterations = num_iterations
        self.centroids = [None] * k

    def train(self, data):

        random.shuffle(data)
        train_data = [np.array(d[:-1], dtype=np.float) for d in data]
        labels = [d[-1] for d in data]

        # randomly initialize centroids
        for i in range(self.k):
            self.centroids[i] = train_data[i]

        for epoch in range(self.num_iterations):
            groups = {idx: [] for idx in range(self.k)}
            results = {idx: [0, 0] for idx in range(self.k)}

            # assign groups
            loss = 0.0
            for d, label in zip(train_data, labels):
                distance = [np.linalg.norm(d - self.centroids[i]) for i in range(self.k)]
                loss += min(distance)
                prediction = distance.index(min(distance))
                if prediction == label:
                    results[label][0] += 1
                results[label][1] += 1
                groups[prediction].append(d)
            loss /= len(train_data)
            print('train loss: {} {}'.format(
                loss,
                ' '.join(['{}/{}'.format(results[i][0], results[i][1]) for i in range(self.k)])))

            # recalculate centroids
            for i in range(self.k):
                self.centroids[i] = np.mean(groups[i], axis=0)


data, labels = read_iris_data()
model = k_means()
model.train(data)
