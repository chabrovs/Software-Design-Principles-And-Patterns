from abc import ABC, abstractmethod


class DatabaseI(ABC):
    @abstractmethod
    def connect(self):
        ...


class SQLDatabase(DatabaseI):
    def connect(self):
        print(f"Connecting to the SQL Database...")
    
        return "SQL Connection"
    

class RedisDatabase(DatabaseI):
    def connect(self):
        print(f"Connection to the Redis Database...")

        return "Redis Connection"


class FactoryI(ABC):
    @abstractmethod
    def create_database(self):
        ...


class SQLDatabaseFactory(FactoryI):
    def create_database(self):
        return SQLDatabase()
    

class RedisDatabaseFactory(FactoryI):
    def create_database(self):
        return RedisDatabase()


def get_database(type: str):
    match type:
        case "sql":
            return SQLDatabaseFactory().create_database().connect()
        case "redis":
            return RedisDatabaseFactory().create_database().connect()
        case _:
            raise NotImplementedError("Not supported")
        

if __name__ == "__main__":
    DB_SQL = get_database("sql")
    DB_Redis = get_database("redis")

    print(DB_SQL) # STDOUT: SQL Connection.
    print(DB_Redis) # STDOUT: Redis Connection.


