from abc import ABC, abstractmethod


# 1. <<Interface>>: Product

class Database(ABC):
    @abstractmethod
    def connect(self):
        ...


# 2. Concrete: Product
class SQLDatabase(Database):
    def connect(self):
        print(f"Connecting to SQL Database...")

        return "SQL Database connection"


class RedisDatabase(Database):
    def connect(self):
        print(f"Connecting to REDIS Database...")

        return "Redis Database connection"


# 3. <<Interface>>: Factory
class DatabaseFactory(ABC):
    @abstractmethod
    def create_database(self) -> Database:
        ...


# 4. Concrete: Factory
class SQLFactory(DatabaseFactory):
    def create_database(self) -> Database:
        return SQLDatabase()


class RedisFactory(DatabaseFactory):
    def create_database(self) -> Database:
        return RedisDatabase()


# 5. Client code
def connect_to_database(database: Database):
    database = database.connect()

    return database


# Usage:
if __name__ == "__main__":
    sql_db = connect_to_database(SQLDatabase())
    print(sql_db)  # STDOUT: SQL Database connection

    redis_db = connect_to_database(RedisDatabase())
    print(redis_db)  # STDOUT: Redis Database connection
