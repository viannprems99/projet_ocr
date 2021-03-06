class PermisClass:
    """A simple example class"""

    def __init__(self,nom,prenom,date_naissance,lieu_naissance,date_creation,date_expiration,lieu_creation,categorie,numero_permis):
        self.nom= nom
        self.prenom= prenom
        self.date_naissance= date_naissance
        self.lieu_naissance= lieu_naissance
        self.date_creation= date_creation
        self.date_expiration = date_expiration
        self.lieu_creation= lieu_creation
        self.categorie= categorie
        self.numero_permis = numero_permis




    def calcul(self, x,y):
        return x+y

class CarteGrise:

    def __init__(self,num_immatriculation, date_immatriculation, nom, prenom, adresse, marque, version, code_identification, categorie, genre_national, carrosserie, cylindre, puissance, type_carburant, date_visite_technique):
        self.num_immatriculation=num_immatriculation
        self.date_immatriculation=date_immatriculation
        self.nom = nom
        self.prenom = prenom
        self.adresse=adresse
        self.marque=marque
        self.version=version
        self.code_identification=code_identification
        self.categorie=categorie
        self.genre_national=genre_national
        self.carrosserie=carrosserie
        self.cylindre=cylindre
        self.puissance=puissance
        self.type_carburant=type_carburant
        self.date_visite_technique=date_visite_technique

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def calcul(self, x,y):
        return x+y




class CarteIdentite:
    """A simple example class"""

    def __init__(self,nom,prenom,sexe,nationalite,date_naissance,lieu_naissance,nom_usage,numero_document,date_expiration,numero_carte,taille,date_delivrance,adresse):
        self.nom= nom
        self.prenom= prenom
        self.sexe=sexe
        self.nationalite=nationalite
        self.date_naissance= date_naissance
        self.lieu_naissance= lieu_naissance
        self.nom_usage=nom_usage
        self.numero_document=numero_document
        self.date_expiration = date_expiration
        self.numero_carte = numero_carte
        self.taille = taille
        self.date_delivrance = date_delivrance
        self.adresse = adresse
