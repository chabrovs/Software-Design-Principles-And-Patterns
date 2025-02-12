"""
The Protection Proxy encapsulates access to the "Real object" \
and validates whether or not the user can get the access to the "Real Object"
"""


class RealDatabase:
    """
    The 'RealDatabase' is the "Real object" the access to the methods \
    needs to be restricted to.
    """

    def query(self, sql):
        return f"Executing '{sql}'"


# Protection Proxy class
class DatabaseProxy:
    """
    The Proxy class that validates all incoming request to use the \
    'ReadDatabase' object's methods. The Proxy class should implement \
    the same interface that the 'ReadDatabase' class.
    """

    def __init__(self, user_role):
        self._user_role = user_role
        self._real_database = RealDatabase()

    def query(self, sql):
        if self._user_role != "admin":
            return "Access Denied: You do not have permission query the database."

        return self._real_database.query(sql)


# Client code
if __name__ == "__main__":
    db_admin = DatabaseProxy("admin")
    db_guest = DatabaseProxy("guest")

    print(db_admin.query("SELECT * FROM users"))
    print(db_guest.query("SELECT * FROM users"))
