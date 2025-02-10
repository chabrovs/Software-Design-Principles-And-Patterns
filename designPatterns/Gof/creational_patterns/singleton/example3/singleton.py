class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def connect(self):
        return "Connected..."
    

if __name__ == "__main__":
    d1 = DatabaseConnection()
    d2 = DatabaseConnection()

    print(d1 is d2) # STDOUT: True