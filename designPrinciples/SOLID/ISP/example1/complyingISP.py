from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        ...


class Relational(Database):
    @abstractmethod
    def get_table_by_name(self, name: str):
        ...


class NonRelational(Database):
    @abstractmethod
    def retrieve_data(self, data):
        ...


class SQL(Relational):
    def connect(self):
        print("Connecting to the SQL database...")

    def get_table_by_name(self, name):
        return f"Got table '{name}'"
    

class NoSQL(NonRelational):
    def connect(self):
        print("Connecting to the NoSQL database...")
    
    def retrieve_data(self, data):
        return f"Got data '{data}'"
    

if __name__ == "__main__":
    sql = SQL()
    sql.connect()
    print(sql.get_table_by_name("table_workers"))

    noSql = NoSQL()
    noSql.connect()

    print(noSql.retrieve_data("workers_data"))


# This module complies to the ISP.  