from database_spatial import DatabaseSpatial

if __name__ == '__main__':
    # show_point_cloud_from_file()
    db = DatabaseSpatial(database_name="pdb_spatial_db",
                  user_name="admin",
                  password="admin",
                  host="localhost",
                  port=5432)

    db.create_connection()
    # bacha na ukládání dat vícekrát...pak se to hodně zpomalí
    db.load_data_to_db("../PBD_data/DMR5G.xyz")
