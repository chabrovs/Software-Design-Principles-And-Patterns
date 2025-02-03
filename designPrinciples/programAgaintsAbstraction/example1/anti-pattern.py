class FileLogger:
    def log(self, message):
        with open("log.txt", 'a') as file:
            file.write(message + "\n")


class Application:
    def __init__(self):
        self.logger = FileLogger()

    def run(self):
        self.logger.log("Application is running")