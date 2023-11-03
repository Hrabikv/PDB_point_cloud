import numpy as np
import matplotlib.pyplot as plt
from database import database


def show_point_cloud():
    f = open("../PBD_data/DMR5G.xyz", "r")
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


if __name__ == '__main__':
    # show_point_cloud()
    db = database(database_name="pdb_spatial_db",
                  user_name="admin",
                  password="admin",
                  host="localhost",
                  port=5432)

    db.create_connection()
    print(db.select_from_database())
    db.close_connection()
