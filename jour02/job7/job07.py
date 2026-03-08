import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root_1234",
    database="staff",
    ssl_disabled=True
)

curseur = connexion.cursor()
curseur.execute("SELECT * FROM employe WHERE salaire > 3000;")
resultat = curseur.fetchall()
print(resultat)

curseur = connexion.cursor()
curseur.execute("SELECT employe.nom, employe.prenom, service.nom FROM employe JOIN service ON employe.id_service = service.id;")
resultat = curseur.fetchall()
print(resultat)

class Employe:
    def __init__(self,connexion):
        self.connexion = connexion
        
    def Create(self, nom, prenom, salaire, id_service):
        curseur = self.connexion.cursor()
        curseur.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s,%s,%s,%s)",(nom, prenom, salaire, id_service))
        self.connexion.commit()
        
    def Read(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM employe")
        return curseur.fetchall()
        
    def Update(self,id, nom, prenom, salaire, id_service):
        curseur = self.connexion.cursor()
        curseur.execute("UPDATE employe SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s",(nom, prenom, salaire, id_service, id))
        self.connexion.commit()

    def Delete(self,id):
        curseur = self.connexion.cursor()
        curseur.execute("DELETE FROM employe WHERE id=%s",(id,))
        self.connexion.commit()
        
emp = Employe(connexion)
print(emp.Create("Test","User",2000,2))
print(emp.Read())
print(emp.Update(7, "Test", "Modifie", 2500, 1))
print(emp.Delete(7))