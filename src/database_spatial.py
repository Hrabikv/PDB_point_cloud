from sqlalchemy import create_engine
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point  # Import the Point class if it's not already imported
import numpy as np
import matplotlib.pyplot as plt
import psycopg2


class DatabaseSpatial:

    def __init__(self,
                 database_name,
                 user_name,
                 password,
                 host,
                 port):
        self.database_name=database_name
        self.user_name=user_name
        self.password=password
        self.host=host
        self.port=port
        self.connection = None
        self.engine = None

    def create_connection(self):
        self.connection = psycopg2.connect(
            database=self.database_name,
            user=self.user_name,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.engine = create_engine(self.conn_string())

    def conn_string(self):
        return f"postgresql://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.database_name}"

    def load_data_to_db(self, inputfile):
        df = pd.read_table(inputfile, skiprows=0, delim_whitespace=True, names=['x', 'y', 'z'])
        print(df.head(3))

        # Create a GeoSeries with Point objects from the x and y columns
        geometry = [Point(x, y) for x, y in zip(df['x'], df['y'])]

        # Create the GeoDataFrame and set the geometry column
        gdf = gpd.GeoDataFrame(df, geometry=geometry)
        gdf.crs = "EPSG:4326"
        gdf.to_postgis("pilsen", self.engine, if_exists="append", chunksize=10000)

    def select_from_database(self, limit=0):
        cursor = self.connection.cursor()
        if (limit):
            query = f"SELECT x, y, z, geometry FROM public.pilsen LIMIT {limit}"
            cursor.execute(query)
        else:
            cursor.execute("SELECT x, y, z, geometry FROM public.pilsen")
        records = cursor.fetchall()
        cursor.close()
        return records

    def close_connection(self):
        self.connection.close()
