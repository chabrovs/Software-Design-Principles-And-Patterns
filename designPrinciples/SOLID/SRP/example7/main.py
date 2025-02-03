import config


def connect_to_server(address):
    print(f"Connected to the server '{address}'")


if __name__ == "__main__":
    connect_to_server(config.EMAIL_SERVER)