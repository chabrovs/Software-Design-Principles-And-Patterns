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


class LoggerFactory:
    @staticmethod
    # Dependency Inversion as the abstract class is set as the return type but not a concrete class.
    def get_logger(logger_type: str) -> Logger:
        match logger_type:
            case "file":
                return FileLogger()
            case "console":
                return ConsoleLogger()
            case _:
                raise ValueError(f"Logger '{logger_type}' does not exits!")


class Application:
    # Dependency inversion and Dependency injection.
    def __init__(self, logger: Logger):
        self._logger = logger  # Encapsulation and access modification.

    def run(self):
        self._logger.log("Application is running")


if __name__ == '__main__':
    logger_factory = LoggerFactory()

    app1 = Application(logger_factory.get_logger("file"))
    app2 = Application(logger_factory.get_logger("console"))
    # app2 = Application(logger_factory.get_logger("database")) # STDERR: ValueError: Logger 'database' does not exits!

    app1.run()
    app2.run()
