import numpy as np

class ART2:
    def __init__(self, vigilance=0.8):
        self.vigilance = vigilance
        self.categories = []

    def train(self, inputs):
        for x in inputs:
            x = np.array(x, dtype=float)
            norm = np.linalg.norm(x)

            if norm != 0:
                x = x / norm

            assigned = False

            for i, weight in enumerate(self.categories):
                similarity = np.dot(x, weight)

                if similarity >= self.vigilance:
                    print(x, "belongs to Cluster", i + 1)
                    assigned = True
                    break

            if not assigned:
                self.categories.append(x.copy())
                print(x, "belongs to Cluster",
                      len(self.categories))

inputs = [
    [0.9, 0.1],
    [0.8, 0.2],
    [0.1, 0.9],
    [0.2, 0.8]
]

model = ART2(vigilance=0.95)
model.train(inputs)