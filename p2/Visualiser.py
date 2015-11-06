import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

class Visualiser:

    def __init__(self, filename_training_data):
        return

    @staticmethod
    def tSNE_plot2(features, labels):
        """Do dimension reduction to 2 dimensions with t-SNE and plot the result."""
        model = TSNE(n_components=2, random_state=0)
        transformed = model.fit_transform(features)

        print("Data transformed, now plotting...")

        # Plotting
        x = transformed[:, 0]
        y = transformed[:, 1]
        colors = labels

        plt.scatter(x, y, c=colors)
        plt.show()

    @staticmethod
    def tSNE_plot3(features, labels):
        """Do dimension reduction to 2 dimensions with t-SNE and plot the result."""
        model = TSNE(n_components=3, random_state=0)
        transformed = model.fit_transform(features)

        print("Data transformed, now plotting...")

        # Plotting
        x = transformed[:, 0]
        y = transformed[:, 1]
        z = transformed[:, 2]
        colors = labels

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, s=20, c=colors, depthshade=True)
        plt.show()