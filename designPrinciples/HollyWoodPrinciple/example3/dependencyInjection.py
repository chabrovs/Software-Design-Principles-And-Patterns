class Logger:
    def log(self, message: str):
        print(f"Logging: {message}")


class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log("The application is running...")


if __name__ == "__main__":
    app = Application(Logger())
    app.run()


# The higher-level component (Application) does not create or control the 'Logger'.
# Instead, it's injected from the outside.
