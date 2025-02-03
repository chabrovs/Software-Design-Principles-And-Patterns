class Database:
    def connect(self):
        print("Connecting to database.")


class UserService:
    def __init__(self):
        self._database = None # Encapsulating _database.

    @property
    def database(self):
        if self._database is None:
            raise ValueError("Database currently has not been set!")
        return self._database 
    
    @database.setter
    def database(self, db):
        if not isinstance(db, Database):
            raise TypeError("Expected a database instance.")
        self._database = db
    
    def get_users(self):
        self.database.connect()
        print("Fetching users")


if __name__ == "__main__":
    service = UserService()
    db = Database()

    service.database = db
    service.get_users()