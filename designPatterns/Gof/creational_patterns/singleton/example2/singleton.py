def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return cls

    return get_instance


@singleton
class Logger:
    def log(self, message):
        print(f"[LOG]: '{message}'")


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    print(logger1 is logger2)


# Singleton using a decorator
