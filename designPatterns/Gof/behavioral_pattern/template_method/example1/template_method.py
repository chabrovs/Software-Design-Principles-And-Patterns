"""
This module implements the Template Method design pattern.
"""


from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    """
    This class represents the 'Abstract Class (or Template Class)'
    """

    def generate_report(self):
        """
        This method represents the 'Algorithm skeleton (or Template Method)'
        """

        self.generate_header()
        self.generate_content()
        self.generate_footer()

    def generate_header(self):
        """
        This method represents a base algorithm step.
        """

        print("Generating Report header")

    def generate_footer(self):
        """
        This method represents a base algorithm step.
        """

        print("Generating Report footer")

    @abstractmethod
    def generate_content(self):
        """
        This class represents an abstract step that must be implemented by \
        subclasses
        """

        ...


class PDFReport(ReportGenerator):
    """
    This class represents a 'Concrete Class'
    """

    def generate_content(self):
        print("Generating PDF content")


class HTMLReport(ReportGenerator):
    """
    This class represents a 'Concrete Class'
    """

    def generate_content(self):
        print("Generating HTML content")


# Client code
if __name__ == "__main__":
    pdf_report = PDFReport()
    pdf_report.generate_report()

    print("---")

    html_report = HTMLReport()
    html_report.generate_report()
