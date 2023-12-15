import numpy as np
import plotly.graph_objects as go


def show_db_point_cloud(data):
    x = [item[0] for item in data]
    y = [item[1] for item in data]
    z = [item[2] for item in data]
    max_x = np.max(x)
    max_y = np.max(y)
    max_z = np.max(z)
    min_x = np.min(x)
    min_y = np.min(y)
    min_z = np.min(z)

    print("X max: {0}, min: {1}, diff: {2}".format(max_x, min_x, np.abs(max_x - min_x)))
    print("Y max: {0}, min: {1}, diff: {2}".format(max_y, min_y, np.abs(max_y - min_y)))
    print("Z max: {0}, min: {1}, diff: {2}".format(max_z, min_z, np.abs(max_z - min_z)))

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
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),
                      scene=dict(
                          xaxis_title='X AXIS TITLE',
                          yaxis_title='Y AXIS TITLE',
                          zaxis_title='Z AXIS TITLE')
                      )
    fig.show()


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

        max_x = np.max(x)
        max_y = np.max(y)
        max_z = np.max(z)
        min_x = np.min(x)
        min_y = np.min(y)
        min_z = np.min(z)

        print("X max: {0}, min: {1}, diff: {2}".format(max_x, min_x, np.abs(max_x - min_x)))
        print("Y max: {0}, min: {1}, diff: {2}".format(max_y, min_y, np.abs(max_y - min_y)))
        print("Z max: {0}, min: {1}, diff: {2}".format(max_z, min_z, np.abs(max_z - min_z)))

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
