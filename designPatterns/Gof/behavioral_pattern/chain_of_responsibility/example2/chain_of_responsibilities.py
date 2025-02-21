"""
This module implement a multilevel logging system utilizing the \
Chain of Responsibility (CoR) design pattern.
"""


from abc import ABC, abstractmethod


class Logger(ABC):
    """
    This class represents the 'Handle Interface'.
    """
    INFO, WARNING, ERROR = 1, 2, 3

    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, logger):
        self.next_logger = logger

        return logger

    def log(self, level, message):
        if self.level <= level:
            self.write_log(message)

        if self.next_logger:
            self.next_logger.log(level, message)

    @abstractmethod
    def write_log(self, message):
        ...


class ConsoleLogger(Logger):
    """
    This class is a concrete handler.
    """

    def write_log(self, message):
        print(f"[CONSOLE]: '{message}'")


class FileLogger(Logger):
    """
    This class is a concrete handler.
    """

    def write_log(self, message):
        print(f"[FILE]: '{message}'")


class EmailLogger(Logger):
    """
    This class is a concrete handler.
    """

    def write_log(self, message):
        print(f"[EMAIL]: '{message}'")


# Client code
if __name__ == "__main__":
    # 1. Init loggers
    console_logger = ConsoleLogger(Logger.INFO)
    file_logger = FileLogger(Logger.WARNING)
    email_logger = EmailLogger(Logger.ERROR)

    # 2. Build the chain
    console_logger.set_next_logger(file_logger).set_next_logger(email_logger)

    # 3. Usage
    # Console logger
    console_logger.log(Logger.INFO, "This is a info message.")
    # Console logger + File logger
    console_logger.log(Logger.WARNING, "This is warning message")
    # Console logger + File logger + Email logger
    console_logger.log(Logger.ERROR, "This is error message")
