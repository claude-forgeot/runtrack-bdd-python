from database import get_connection 


class Product:
    def __init__(self):
        self.connection = get_connection()

    # Create
    def create(self, name, description, price, quantity, id_category):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO product (name, description, price, quantity,id_category)VALUES (%s, %s, %s, %s, %s)", (name, description, price, quantity, id_category))
        self.connection.commit()

    # Read
    def read(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT product.id,product.name,product.description,product.price,product.quantity,category.name FROM product JOIN category ON product.id_category = category.id")
        return cursor.fetchall() or []

    # Update
    def update(self, id, name, description, price, quantity, id_category):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE product SET name=%s, description=%s, price=%s,quantity=%s, id_category=%s WHERE id=%s", (name, description, price, quantity, id_category, id))
        self.connection.commit()

    # Delete
    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM product WHERE id=%s", (id,))
        self.connection.commit()

    # Filter by category
    def filter(self,name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT product.id,product.name,product.description,product.price,product.quantity,category.name FROM product JOIN category ON product.id_category = category.id WHERE category.name = %s",(name,))
        return cursor.fetchall() or []