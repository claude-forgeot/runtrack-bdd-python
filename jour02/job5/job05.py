import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root_1234",
    database="LaPlateforme",
    ssl_disabled=True
)

curseur = connexion.cursor()
curseur.execute("SELECT SUM(superficie) FROM ETAGE;")
resultat = curseur.fetchall()
print(f"La superficie de La Plateforme est de {resultat[0][0]}m². Vue mer sur l'ensemble de la Plateforme.")