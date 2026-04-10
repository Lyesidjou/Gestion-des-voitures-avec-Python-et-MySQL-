from crud_db import connecter_db
from crud_db import ajouter_voiture
from voiture import Voiture

con=connecter_db()
print(con)
con.close()

v1=Voiture("HONDA","Civic",2018,34000)
v2=Voiture("Toyota","Supra",2019,67000)
v3=Voiture("Buggati","Chiron",2018,3000000)
v4=Voiture("Lamborgini","Huracan",2012,500000)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)
ajouter_voiture(v4)

