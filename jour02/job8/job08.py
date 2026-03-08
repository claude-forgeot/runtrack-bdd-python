import mysql.connector

# Connector
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root_1234",
    database="zoo",
    ssl_disabled=True
)

class Animal:
    def __init__(self,connexion):
        self.connexion = connexion
        
    def create(self, nom, race, id_cage, date_naissance, pays_origine):
        curseur = self.connexion.cursor()
        curseur.execute("INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s,%s,%s,%s,%s)",(nom, race, id_cage, date_naissance, pays_origine))
        self.connexion.commit()
        
    def read(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM animal")
        return curseur.fetchall()
        
    def update(self,id, nom, race, id_cage, date_naissance, pays_origine):
        curseur = self.connexion.cursor()
        curseur.execute("UPDATE animal SET nom=%s, race=%s, id_cage=%s, date_naissance=%s, pays_origine=%s WHERE id=%s",(nom, race, id_cage,date_naissance,pays_origine, id))
        self.connexion.commit()

    def delete(self,id):
        curseur = self.connexion.cursor()
        curseur.execute("DELETE FROM animal WHERE id=%s",(id,))
        self.connexion.commit()

    def afficherAnimaux(self,id_cage):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM animal WHERE id_cage = %s", (id_cage,))
        resultat = curseur.fetchall()
        print(f"Il y a actuellement {resultat} animaux présents.")

    def deplacer(self, id, id_cage):
        curseur = self.connexion.cursor()
        curseur.execute("UPDATE animal SET id_cage=%s WHERE id=%s",(id_cage,id))
        self.connexion.commit()

class Cage:
    def __init__(self,connexion):
        self.connexion = connexion
        
    def create(self, superficie, capacite):
        curseur = self.connexion.cursor()
        curseur.execute("INSERT INTO cage (superficie,capacite) VALUES (%s,%s)",(superficie,capacite))
        self.connexion.commit()
        
    def read(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM cage")
        return curseur.fetchall()
        
    def update(self,id, superficie, capacite):
        curseur = self.connexion.cursor()
        curseur.execute("UPDATE cage SET superficie=%s, capacite=%s WHERE id=%s",(superficie,capacite, id))
        self.connexion.commit()

    def delete(self,id):
        curseur = self.connexion.cursor()
        curseur.execute("DELETE FROM cage WHERE id=%s",(id,))
        self.connexion.commit()

    def superficieTotale(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT SUM(superficie) FROM cage")
        resultat = curseur.fetchall()
        print(f"La superficie totale est de : {resultat}m².")

animal1 = Animal(connexion)
cage1 = Cage(connexion)

while True :
    type = input("Animal ou Cage ? (a/c/q pour quitter) : ")
    if type == "q": 
        break
    
    if type == "a":
        choix = input("1:Ajouter, 2:Afficher, 3: Deplacer, 4:Modifier, 5:Supprimer. :")
        if choix =="1":
            animal1.create(input("Nom ? : "),input("Race ? : "),input("Numéro de cage ? : "),input("Date de naissance ? : "),input("Pays d'origine ? : "))
        elif choix =="2":
            print(animal1.read())
        elif choix == "3":
            animal1.deplacer(input("ID de l'animal a déplacer ? : "), input("Nouvelle cage ? : "))
        elif choix == "4":
            animal1.update(input("ID ? :"),input("Nom ? : "),input("Race ? : "),input("Numéro de cage ? :"),input("Date de naissance ? :"),input("Pays d'origine ? :"))
        elif choix == "5":
            animal1.delete(input("ID de l'animal à supprimer ? : "))
        else :
            break
    
    elif type == "c":
        choix = input("1:Ajouter, 2:Afficher, 3:Modifier, 4:Supprimer, 5:Animaux par cage, 6:Superficie totale. :")
        if choix == "1":
            cage1.create(input("Superficie ? : "), input("Capacité ? : "))
        elif choix == "2":
            print(cage1.read())
        elif choix == "3":
            cage1.update(input("ID de la cage ? : "), input("Superficie ? : "), input("Capacite ? : "))
        elif choix == "4":
            cage1.delete(input("ID de la cage à supprimer ? : "))
        elif choix == "5":
            animal1.afficherAnimaux(input("ID de la cage : "))
        elif choix == "6":
            cage1.superficieTotale()
        else:
            break
