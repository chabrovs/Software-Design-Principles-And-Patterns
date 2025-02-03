class Middleware:
    def execute(self):
        ...


class AuthenticationMiddleware(Middleware):
    def execute(self, data):
        print("Authenticating user.")
        return data
    

class LoggingMiddleware(Middleware):
    def execute(self, data):
        print("Logging request.")
        return data
    


if __name__ == "__main__":
    # Initialise enabled middleware 
    enabled_middleware_list = [AuthenticationMiddleware(), LoggingMiddleware()]

    data = {}

    for middleware in enabled_middleware_list:
        data = middleware.execute(data)


# This module adheres the OCP because it allows to add new functionality \
# by creating and enabling new middlewares without the need to modify \
# existing code.   