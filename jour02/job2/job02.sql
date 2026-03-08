
mysql> CREATE TABLE ETAGE (
    -> id INT PRIMARY KEY AUTO_INCREMENT,
    -> nom VARCHAR(255),
    -> numero INT,
    -> superficie INT
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> CREATE TABLE SALLE (
    -> id INT PRIMARY KEY AUTO_INCREMENT,
    -> nom VARCHAR(255),
    -> id_etage INT,
    -> capacite INT
    -> );
Query OK, 0 rows affected (0.03 sec)

