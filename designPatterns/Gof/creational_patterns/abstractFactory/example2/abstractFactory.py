from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        ...


class QueryExecutor(ABC):
    @abstractmethod
    def execute(self, query: str):
        ...


class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        ...

    @abstractmethod
    def create_query_executer(self) -> QueryExecutor:
        ...


class PostgresConnection(DatabaseConnection):
    def connect(self):
        return "Postgres connection"


class RedisConnection(DatabaseConnection):
    def connect(self):
        return "Redis connection"


class PostgresExecuter(QueryExecutor):
    def execute(self, query):
        return f"The query '{query}' executed in Postgres"


class RedisExecuter(QueryExecutor):
    def execute(self, query):
        return f"The query '{query}' executed in Redis"


class PostgresFactory(DatabaseFactory):
    def create_connection(self):
        return PostgresConnection()

    def create_query_executer(self):
        return PostgresExecuter()


class RedisFactory(DatabaseFactory):
    def create_connection(self):
        return RedisConnection()

    def create_query_executer(self):
        return RedisExecuter()

# Client


def execute_database_operations(factory: DatabaseFactory):
    connection = factory.create_connection()
    executer = factory.create_query_executer()

    print(connection.connect())
    print(executer.execute("SELECT * FROM Engineers"))


if __name__ == "__main__":
    postgres = PostgresFactory()
    redis = RedisFactory()

    execute_database_operations(postgres)
    execute_database_operations(redis)
