class UserCreator:
    def create_user(self, username, email):
        print(f"User '{username}' created '{email}'")
    

class EmailValidator: 
    def validate_email(self, email):
        if "@" not in email:
            return ValueError("Email is invalid.")


class EmailSender:
    def send_and_welcome(self, email):
        print(f"Welcome email send to '{email}'")


if __name__ == "__main__":
    user_creator = UserCreator()
    user_creator.create_user("Sergei", "me@chabrovs.tech")

    email_validator = EmailValidator()
    email_validator.validate_email("me@chabrovs.tech")

    email_sender = EmailSender()
    email_sender.send_and_welcome("me@chabrovs.tech")


# Now each class has its own limited responsibilities.
# In this example the module adheres to the SRP. 