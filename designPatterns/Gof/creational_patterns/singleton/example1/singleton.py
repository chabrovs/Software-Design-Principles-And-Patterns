class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2) # STDOUT: True. 


# Singleton using a class variable. 