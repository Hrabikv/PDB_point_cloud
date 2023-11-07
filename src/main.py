import pandas as pd
import geopandas as gpd
from shapely.geometry import Point  # Import the Point class if it's not already imported
import numpy as np
import matplotlib.pyplot as plt
from database_spatial import DatabaseSpatial
from plot_from_database import show_db_point_cloud


def show_point_cloud_from_file():
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
    #show_point_cloud_from_file()
    db = DatabaseSpatial(database_name="pdb_spatial_db",
                  user_name="admin",
                  password="admin",
                  host="localhost",
                  port=5432)

    db.create_connection()
    #db.load_data_to_db("../PBD_data/DMR5G.xyz")

    # LIMIT 2
    print(db.select_from_database(2))

    show_db_point_cloud(db.select_from_database())
    db.close_connection()
