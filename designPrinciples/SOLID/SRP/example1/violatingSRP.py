class Report:
    def generate_report(self, data):
        # Business logic for generating report.
        return f"Report generated with data {data}"

    def save_to_file(self, file_path, content):
        # File handling logic.
        with open(file_path, "w") as file:
            file.write(content)

    def send_email(self, email, content):
        # Email sending logic.
        print(f"Sending report to {email}: {content}")


if __name__ == "__main__":
    report = Report()
    new_report = report.generate_report("New report")
    report.save_to_file("new_report.txt", new_report)
    report.send_email("me@chabrovs.tech", new_report)


# Problems:
# 1. Generating reports (business logic)
# 2. Saving reports to files (handling logic)
# 3. Sending report by email (communication logic)
# There are three different independent responsibilities \
# Change to one responsibility might break others.
