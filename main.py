from crud_db import connecter_db
con=connecter_db()
print(con)
con.close()