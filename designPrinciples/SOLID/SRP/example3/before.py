class UserManager:
    def create_user(self, username, email):
        print(f"User {username} '{email}' created")
    
    def validate_email(self, email):
        if "@" not in email:
            return ValueError("Email is invalid.")

    def send_and_welcome(self, email):
        print(f"Welcome email send to '{email}'")


if __name__ == "__main__":
    user_manager = UserManager()

    user_manager.create_user("Sergei", "me@chabrovs.tech")

    user_manager.validate_email("me@chabrovs.tech")

    user_manager.send_and_welcome("me@chabrovs.tech")


# Problem:
# The 'UserManager' class has too many unrelated responsibilities.
# such as sending email validation, user creation and email sending.
# Solution Decompose these responsibilities into different classes 
# See 'example3/after.py