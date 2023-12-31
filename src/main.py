from database_spatial import DatabaseSpatial
from plot_from_database import show_db_point_cloud, show_point_cloud_from_file

if __name__ == '__main__':
    # show_point_cloud_from_file()
    db = DatabaseSpatial(database_name="pdb_spatial_db",
                  user_name="admin",
                  password="admin",
                  host="localhost",
                  port=5432)

    db.create_connection()

    # LIMIT 2
    print(db.select_from_database(2))

    show_db_point_cloud(db.select_from_database())
    db.close_connection()
