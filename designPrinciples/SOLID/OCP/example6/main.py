from abc import ABC, abstractmethod
import json
import os


class Logger(ABC):
    def __init__(self):
        self._config

    @abstractmethod
    def log(self, message: str) -> None:
        ...


class ConsoleLogger(Logger):
    def __init__(self, config):
        self._config = config

    def log(self, message):
        print(f"[CONSOLE LOG]: {message}")


class FileLogger(Logger):
    def __init__(self, config):
        self._config = config

    def log(self, message):
        print(f"[FILE LOG]: {message}")


class Application:
    def __init__(self, logger: Logger):
        self._logger = logger

    def run(self):
        self._logger.log("Application is running...")


class LoggerFactory:
    @staticmethod
    def get_logger_config(file_path: str) -> dict:
        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), file_path)
        with open(file_path) as file:
            config = json.load(file)

        return config

    @staticmethod
    def get_logger(config: dict):
        logger_type = config["logging"]

        match logger_type:
            case "console":
                return ConsoleLogger(config)
            case "file":
                return FileLogger(config)


if __name__ == "__main__":
    logger_factory = LoggerFactory()
    config = logger_factory.get_logger_config("settings.json")

    logger = logger_factory.get_logger(config)

    app = Application(logger)
    app.run()


# This example adheres to the OCP because it allows to change \
# the functionality dynamically by altering setting.json parameters \
# Also, this module support implementation of new functionality by \
# creating new concrete classes without modifying existing ones.
