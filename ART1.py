
import numpy as np

class ART1:
    def __init__(self, vigilance=0.7):
        self.vigilance = vigilance
        self.categories = []

    def train(self, inputs):
        for x in inputs:
            assigned = False

            for i, weight in enumerate(self.categories):
                intersection = np.sum(x * weight)
                match = intersection / (np.sum(x) + 1e-10)

                if match >= self.vigilance:
                    self.categories[i] = x * weight
                    print(x, "belongs to Cluster", i + 1)
                    assigned = True
                    break

            if not assigned:
                self.categories.append(x.copy())
                print(x, "belongs to Cluster", len(self.categories))

inputs = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0]
])

model = ART1(vigilance=0.6)
model.train(inputs)