import pandas as pd
# import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=2,
            color=z,  # set color to an array/list of desired values
            colorscale='RainBow',  # choose a colorscale
            opacity=1
        )
    )])

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    #
    # color_map = plt.get_cmap('RdYlGn')
    #
    # n = len(x)
    # #
    # # n = 4000
    #
    # print("X max: {0}, min: {1}, diff: {2}".format(np.max(x), np.min(x), np.abs(np.max(x) - np.min(x))))
    # print("Y max: {0}, min: {1}, diff: {2}".format(np.max(y), np.min(y), np.abs(np.max(y) - np.min(y))))
    # print("Z max: {0}, min: {1}, diff: {2}".format(np.max(z), np.min(z), np.abs(np.max(z) - np.min(z))))
    #
    # ax.scatter(x[:n], y[:n], z[:n], marker="x", c=z[:n], cmap=color_map)
    #
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    #
    # plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_point_cloud()
