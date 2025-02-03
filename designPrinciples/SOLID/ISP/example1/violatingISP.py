from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def get_table_by_name(self, name: str):
        ...


class SQL(Database):
    def connect(self):
        print("Connecting to the SQL database...")

    def get_table_by_name(self, name):
        return f"Got table '{name}'"
    

class NoSQL(Database):
    def connect(self):
        print("Connecting to the NoSQL database...")
    
    def get_table_by_name(self, name):
        raise NotImplementedError("NoSQL database does not have tables!")
    

if __name__ == "__main__":
    sql = SQL()
    sql.connect()
    print(sql.get_table_by_name("table_workers"))

    noSql = NoSQL()
    noSql.connect()

    noSql.get_table_by_name("table_workers")


# This module violates the ISP because \
# there is a big general-purpose interface that forces concrete classes \
# implement methods that do not support by nature.  
# See 'example1/complyingISP.py' to fix it.   