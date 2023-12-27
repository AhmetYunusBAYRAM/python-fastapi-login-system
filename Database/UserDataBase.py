from Models.UserModel import UserModel
from Models.LoginModel import LoginModel
from Database.DatabaseHandler import DatabaseHandler
from Enum.DataBaseEnum import DataBaseEnum
from Models.ResponseModel import ResponseModel
import secrets
class UserDatabase:

    def login_user_email_and_password(loginModel : LoginModel):
        database_handler = DatabaseHandler(DataBaseEnum.Cebinde_DB.value)
        database_handler.connect()

        user_id = UserDatabase.control_password_email(loginModel, database_handler)
        return user_id

    def create_user_account(userModel : UserModel):
        database_handler = DatabaseHandler(DataBaseEnum.Cebinde_DB.value)
        database_handler.connect()

        if UserDatabase.email_exists(userModel.user_email,database_handler):
            return ResponseModel(code = 400, message = "Bu mail adresine ait hesap bulunmaktadır.",data = {"email":userModel.user_email})
        else:
            insert_userDetail_query = """
                   INSERT INTO user_details 
                   (user_id, user_profile_image, user_first_name, user_last_name, user_email, user_login_type_id, user_country_id) 
                   VALUES (%(user_id)s, %(user_profile_image)s, %(user_first_name)s, %(user_last_name)s, %(user_email)s, %(user_login_type)s, %(user_country_id)s)
                   """

            insert_userAuth_query = """
                   INSERT INTO user_auth 
                   (user_id, user_email, user_password) 
                   VALUES (%(user_id)s, %(user_email)s, %(user_password)s)
                   """

            userModel.user_id = secrets.token_urlsafe(20)

            database_handler.cursor.execute(insert_userDetail_query, vars(userModel))
            database_handler.cursor.execute(insert_userAuth_query, vars(userModel))

            database_handler.conn.commit()
            database_handler.disconnect()
            return ResponseModel(code=200, message="Kullanıcı başarıyla oluşturuldu.", data = {"email" : userModel.user_email})


        database_handler.disconnect()

    @classmethod
    def email_exists(self,email, database_handler):
        try:
            select_query = "SELECT user_email FROM user_details WHERE user_email = %s"
            database_handler.cursor.execute(select_query, (email,))

            result = database_handler.cursor.fetchone()

            return result

        except database_handler.mysql.connector.Error as err:
            print(f"Hata: {err}")

    @classmethod
    def control_password_email(self, loginModel : LoginModel, database_handler):
        try:
            select_query = "SELECT user_id FROM user_auth WHERE user_email = %(user_email)s and user_password = %(user_password)s"
            database_handler.cursor.execute(select_query, vars(loginModel))
            result = database_handler.cursor.fetchone()

            return result

        except database_handler.mysql.connector.Error as err:
            print(f"Hata: {err}")
