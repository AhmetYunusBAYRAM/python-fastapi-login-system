from Database.DatabaseHandler import DatabaseHandler
from Enum.DataBaseEnum import DataBaseEnum
from Models.TokenModel import TokenModel
from datetime import datetime, timedelta

class TokenDataBase:
    @classmethod
    def delete_token(self):
        print("Delete token çalıştı"),
        print(datetime.now())
        database_handler = DatabaseHandler(DataBaseEnum.Access_Token_DB.value)
        database_handler.connect()

        delete_token_query = """DELETE FROM token_table WHERE expires_in < %s"""
        database_handler.cursor.execute(delete_token_query, (datetime.now(),))

        database_handler.conn.commit()
        database_handler.disconnect()

    def create_token(tokenModel: TokenModel):
        database_handler = DatabaseHandler(DataBaseEnum.Access_Token_DB.value)
        database_handler.connect()

        insert_token_query = """INSERT INTO access_token_db.token_table 
                                (access_token, user_id, expires_in) 
                                VALUES (%(access_token)s, %(user_id)s, %(expires_in)s)"""

        database_handler.cursor.execute(insert_token_query, vars(tokenModel))
        database_handler.conn.commit()
        database_handler.disconnect()

