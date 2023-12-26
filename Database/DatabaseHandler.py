import mysql.connector
class DatabaseHandler:
    def __init__(self,database):
        self.db_config = {
            'host': "localhost",
            'user': "root",
            'password': "my-secret-pw",
            'database': database,
            'port': 3306,
        }

        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)

            if self.conn.is_connected():
                print("Bağlantı başarıyla kuruldu.")
                self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print(f"Hata: {err}")

    def disconnect(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Bağlantı kapatıldı.")