"""
This module implement the Decorator pattern for a class.
"""


from abc import ABC, abstractmethod
import time


class DatabaseOperatorI(ABC):
    """
    The interface (Component interface). This is the interface the client \
    interacts with.
    """

    @abstractmethod
    def query(self, sql: str) -> str:
        ...


class SQLOperator(DatabaseOperatorI):
    """
    The Concrete implementation of the 'DatabaseOperatorI' interface
    """

    def query(self, sql: str) -> str:
        time.sleep(2.1)

        return f"Result for the query '{sql}'"


class DatabaseOperatorDecorator(DatabaseOperatorI):
    """
    This is the base Decorator class (Abstract Decorator). \
    This class must implement the 'Component interface'.
    """

    def __init__(self, db_operator: DatabaseOperatorI):
        self._db_operator = db_operator

    def query(self, sql):
        return self._db_operator.query(sql)


class ExplainAnalyze(DatabaseOperatorDecorator):
    """
    This the the concrete decorator that adds behavior to the default object.
    """

    def query(self, sql):
        print("[ExplainAnalyze Decorator]: Your query was analyzed.")
        return super().query(sql)


class BenchmarkDecorator(DatabaseOperatorDecorator):
    """
    This the the concrete decorator that adds behavior to the default object.
    """

    def query(self, sql):
        start_time = time.perf_counter()

        query_result = super().query(sql)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f"[Benchmark Analyzer]: "
            f"The sql query was completed in {total_time:.6f}")

        return query_result


# Client code
if __name__ == "__main__":
    sql_operator = SQLOperator()
    benchmark = BenchmarkDecorator(sql_operator)
    analyze = ExplainAnalyze(benchmark)

    print(analyze.query("SELECT * FROM users"))