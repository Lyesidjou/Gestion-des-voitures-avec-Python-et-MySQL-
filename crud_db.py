import mysql.connector
import json

from voiture import Voiture


def  connecter_db():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        connexion=mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
        )
        return connexion

def ajouter_voiture(voiture):
    con=connecter_db()
    crs=con.cursor()

    crs.execute(
        "INSERT INTO voiture (marque,modele,annee,prix) VALUES (%s,%s,%s,%s)",
        (voiture.marque,voiture.modele,voiture.annee,voiture.prix)
    )
    con.commit()
    crs.close()
    con.close()

def supprimer_voiture(id):
    con=connecter_db()
    crs=con.cursor()

    crs.execute(
        "DELETE FROM voiture WHERE id = %s",
        (id,)
    )
    con.commit()
    crs.close()
    con.close()

def recuperer_voiture():
    con=connecter_db()
    crs=con.cursor()

    crs.execute("Select marque,modele,annee,prix,id from voiture")
    afficher=crs.fetchall()

    liste_voitures=[]
    for voiture in afficher:
        v=Voiture(voiture[0],voiture[1],voiture[2],voiture[3],voiture[4])
        liste_voitures.append(v)

    crs.close()
    con.close()
    return liste_voitures
def modifier_voiture(voiture):
    con=connecter_db()
    crs=con.cursor()

    crs.execute(
        """UPDATE voiture set marque = %s,modele= %s,annee = %s,prix = %s WHERE id = %s """,
        (voiture.marque,voiture.modele,voiture.annee,voiture.prix,voiture.id))

    con.commit()
    crs.close()
    con.close()







