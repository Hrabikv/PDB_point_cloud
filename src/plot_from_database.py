import numpy as np
import matplotlib.pyplot as plt

def show_db_point_cloud(data):
    x = [item[0] for item in data]
    y = [item[1] for item in data]
    z = [item[2] for item in data]


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