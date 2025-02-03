class ReportGenerator:
    def generate_report(self, data):
        return (f"Report generated with data '{data}'")


class FileSaver:
    def save_file(self, content, file_path):
        with open(file_path, "w") as file:
            file.write(content)


class ReportManager:
    def __init__(self, generator: ReportGenerator, file_saver: FileSaver):
        self.generator = generator
        self.file_saver = file_saver

    def create_and_save_report(self, data, file_path):
        report = self.generator.generate_report(data)
        self.file_saver.save_file(report, file_path)


if __name__ == "__main__":
    report_manager = ReportManager(
        ReportGenerator(),
        FileSaver()
    )
    report_manager.create_and_save_report({"sales": 100}, "report.txt")
