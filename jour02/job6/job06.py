import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root_1234",
    database="LaPlateforme",
    ssl_disabled=True
)

curseur = connexion.cursor()
curseur.execute("SELECT SUM(capacite) FROM SALLE;")
resultat = curseur.fetchall()
print(f"La capacité de toutes les salles est de : {resultat[0][0]}.")