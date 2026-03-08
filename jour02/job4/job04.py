import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root_1234",
    database="LaPlateforme",
    ssl_disabled=True
)

curseur = connexion.cursor()
curseur.execute("SELECT nom,capacite FROM SALLE;")
resultat = curseur.fetchall()
print(resultat)