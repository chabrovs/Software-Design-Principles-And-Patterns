"""
"""


from abc import ABC, abstractmethod


class Database(ABC):
    """
    This class is the interface for concrete implementations (Implementor Interface).
    """

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...

    def query(self, sql):
        ...


class PostgreSQL(Database):
    """
    This class is the concrete implementation of the Implementor Interface.
    """

    def connect(self):
        return "PostgreSQL DB Connection"

    def disconnect(self):
        return "PostgreSQL DB Disconnected"

    def query(self, sql):
        return f"Result for query: '{sql}'"


class MySQL(Database):
    """
    This class is the concrete implementation of the Implementor Interface.
    """

    def connect(self):
        return "MySQL DB Connection"

    def disconnect(self):
        return "MySQL DB Disconnected"

    def query(self, sql):
        return f"Result for query: '{sql}'"


class DatabaseController:
    """
    This class defines a high-level interface, holds reference to the implementor and delegates \
    work to the implementor.
    """

    def __init__(self, database: Database):
        self._db = database

    def connect(self):
        return self._db.connect()

    def disconnect(self):
        return self._db.disconnect()

    def query(self, sql):
        return self._db.query(sql)


class AdvancedController(DatabaseController):
    """
    This class extends behavior of the original "Abstraction".
    """

    def get_connection_info(self):
        return f"Currently connected to the {type(self._db).__name__}"


# Client code
if __name__ == "__main__":
    advanced_controller = AdvancedController(PostgreSQL())
    print(advanced_controller.query("SELECT * FROM users"))
    print(advanced_controller.get_connection_info())
