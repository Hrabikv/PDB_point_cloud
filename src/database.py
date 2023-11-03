import psycopg2


class database:

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

    def create_connection(self):
        self.connection = psycopg2.connect(
            database=self.database_name,
            user=self.user_name,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def select_from_database(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from hello_world_table")
        records = cursor.fetchall()
        cursor.close()
        return records

    def close_connection(self):
        self.connection.close()
