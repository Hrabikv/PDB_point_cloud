import pandas as pd
# import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colormaps
# list(colormaps)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def show_point_cloud():
    f = open("PBD_data/DMR5G.xyz", "r")
    # print(colormaps)
    x = []
    y = []
    z = []

    for line in f:
        split_line = line.split(" ")
        x.append(float(split_line[0]))
        y.append(float(split_line[1]))
        z.append(float(split_line[2]))

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    color_map = plt.get_cmap('RdYlGn')

    n = len(x)
    #
    # n = 4000

    print("X max: {0}, min: {1}, diff: {2}".format(np.max(x), np.min(x), np.abs(np.max(x) - np.min(x))))
    print("Y max: {0}, min: {1}, diff: {2}".format(np.max(y), np.min(y), np.abs(np.max(y) - np.min(y))))
    print("Z max: {0}, min: {1}, diff: {2}".format(np.max(z), np.min(z), np.abs(np.max(z) - np.min(z))))

    ax.scatter(x[:n], y[:n], z[:n], marker="x", c=z[:n], cmap=color_map)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_point_cloud()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# def randrange(n, vmin, vmax):
#     """
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     """
#     return (vmax - vmin)*np.random.rand(n) + vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# n = 100
#
# # For each set of style and range settings, plot n random points in the box
# # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, marker=m)
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()