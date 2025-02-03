class ReportGenerator:
    def generate_report(self, data):
        # Business logic.
        return f"report generated with data {data}"
    

class FileSaver:
    def save_to_file(self, file_path, content):
        with open(file_path, "w") as file:
            file.write(content)


class EmailSender:
    def send_email(self, email, content):
        print(f"Sending report to {email}: {content}")


if __name__ == "__main__":
    data = {"sales": 1000}

    report = ReportGenerator().generate_report(data)
    FileSaver().save_to_file("new_report.txt", report)
    EmailSender().send_email("me@chabrovs.tech", report)


# Advantages:
# 1. Each class has one responsibility. 
# 2. Changes to one responsibility won't affect other responsibilities. 
# 3. Easier to test and maintain code.
# Additionally it is possible ot add an orchestrating class. 