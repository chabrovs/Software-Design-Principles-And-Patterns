class Logger:
    def log(self, message):
        print(f"LOG: '{message}'")


class OrderService:
    def __init__(self):
        pass 

    def place_oder(self, order, logger: Logger):
        logger.log(f"Processing order: '{order}'")
    

if __name__ == "__main__":
    logger = Logger()
    service = OrderService()

    service.place_oder(1, logger)


# The 'OrderService''s method 'place_order' requires a local dependency. \
# The dependency was injected into a particular method of a class, thus \
# available only within the method's scope.  

   