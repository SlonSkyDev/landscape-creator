from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from .terrain import Terrain


def main():
    terr = Terrain(8, 0.5, 0.5, 0.5)

    terrshape = terr.map.shape

    X = np.arange(terrshape[0])
    Y = np.arange(terrshape[1])
    X, Y = np.meshgrid(X, Y)
    Z = terr.map

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, color='b')

    plt.show()


if __name__ == '__main__':
    main()
