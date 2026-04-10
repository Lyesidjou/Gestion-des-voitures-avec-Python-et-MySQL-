class Voiture:
    def __init__(self,marque,modele,annee,prix,id=None):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.id = id

    def afficher_voiture(self):
        print(f"la voiture de la marque {self.marque} modele {self.modele} annee {self.annee} elle coute {self.prix} et l'ID est {self.id}")