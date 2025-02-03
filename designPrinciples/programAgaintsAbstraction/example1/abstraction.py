from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        ...


class FileLogger(Logger):
    def log(self, message: str) -> None:
        with open("log.txt", "a") as file:
            file.write(message + "\n")


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print("[Console log]: %s", message)


class Application:
    def __init__(self, logger: Logger): # Dependency inversion and Dependency injection. 
        self._logger = logger # Encapsulation and access modification.  

    def run(self):
        self._logger.log("Application is running")


if __name__ == '__main__':
    app1 = Application(FileLogger())
    app2 = Application(ConsoleLogger())

    app1.run()
    app2.run()

    