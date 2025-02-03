class Logger:
    def log(self, message):
        print(f"Log: {message}")


class Application:
    def __init__(self, logger):
        self._logger = logger
    
    def run(self):
        self._logger.log("The application is running...")


if __name__ == "__main__":
    app = Application(Logger())
    app.run()


# This module adheres to the OCP because it allows to provide \
# other implementation to the existing application. 
# For example, you can provide a 'DataBaseLogger' to the app \
# that implements the database logging logic. And this functionality \
# extension did not involve the 'Application' class code to be modified.  