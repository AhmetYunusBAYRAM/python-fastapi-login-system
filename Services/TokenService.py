from main import *

@app.get("/all")
def get_all_token():
    response = Response(code=200, data=access_tokens_db, message="Aktif bulunan tüm tokenlar listelenmiştir.")
    return response
