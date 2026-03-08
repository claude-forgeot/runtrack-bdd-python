from database import get_connection 


class Category:
    def __init__(self):
        self.connection = get_connection()

    # Create
    def create(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO category (name) VALUES (%s)", (name,))
        self.connection.commit()

    # Read
    def read(self):
        cursor = self.connection.cursor()
        cursor.execute ("SELECT * FROM category")
        return cursor.fetchall() or []

    # Update
    def update(self, id, name):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE category SET name=%s WHERE id=%s", (name, id))
        self.connection.commit()

    # Delete
    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM category WHERE id=%s", (id,))
        self.connection.commit()

