from abc import ABC, abstractmethod


# 1. Define an abstract interface.
class Database(ABC):
    @abstractmethod
    def save_order(self, order):
        ...


# 2. Implement concrete classes.
class MySQLDatabase(Database):
    def save_order(self, order):
        print(f"Saving order '{order}' to the MySQLDatabase")


class PostgresDatabase(Database):
    def save_order(self, order):
        print(f"Saving order '{order}' to the PostgresDatabase")


# 3. Implementing high-level module containing business rules
class OrderService:
    # Dependency injection and Dependency inversion.
    def __init__(self, database: Database):
        self.database = database

    def process_order(self, order):
        print("Processing order")
        self.database.save_order(order)

# 4. Control flow (Orchestrating layer).


if __name__ == "__main__":
    database = MySQLDatabase()  # Create dependency.
    service = OrderService(database)  # Create service & Inject Dependency.

    service.process_order(1)


# This module adheres to the DIP because it the high-level module \
# 'OrderService' depends on an ABC 'Database' but not a concrete \
# low-level implementation of the 'Database' interface.
