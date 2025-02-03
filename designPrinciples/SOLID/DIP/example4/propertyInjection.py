class Database:
    def connect(self):
        print("Connecting to the database.")


class UserService:
    def __init__(self):
        self.database = None # The dependency is not strictly required.  

    def get_users(self):
        if not self.database: # When the dependency requires, check whether or not it was provided. 
            raise ValueError(f"Database dependency is not set!")

        self.database.connect()
        print("Fetching users")


if __name__ == "__main__":
    service = UserService()

    db = Database()
    service.database = db # Set the dependency
    
    service.get_users()