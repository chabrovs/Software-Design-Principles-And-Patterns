"""
The Caching Proxy enables to cache result from frequently user function.
"""


from time import sleep, perf_counter


def benchmark(func):
    """
    The Decorator that benchmarks the execution speed of the query function.
    """

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func_result = func(*args, **kwargs)
        end_time = perf_counter()

        benchmark_result = end_time - start_time

        print(f"Time: {benchmark_result:.5f}")

        return func_result
    return wrapper


class RealDatabase:
    def query(self, sql):
        sleep(2)

        return f"Result for the '{sql}'"


# Caching Proxy
class CacheProxy:
    """
    The 'CacheProxy' class is responsible for caching the queries that were \
    previously executed. The 'CacheProxy' class should implement the \
    'RealDatabase' interface.
    """

    def __init__(self):
        self._real_database = RealDatabase()
        self._cache = {}

    @benchmark
    def query(self, sql):
        if sql not in self._cache:
            query_result = self._real_database.query(sql)
            self._cache[sql] = query_result

        return self._cache.get(sql)


# Client code
if __name__ == "__main__":
    db = CacheProxy()
    print(db.query("SELECT * FROM users"))
    print(db.query("SELECT * FROM users"))
