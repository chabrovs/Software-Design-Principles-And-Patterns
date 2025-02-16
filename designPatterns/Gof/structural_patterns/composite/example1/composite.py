"""
This models implement the Composite design pattern. \
Object: File System. \
Problem: There is the requirement to treat each component of the FS uniformly.
"""


from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """
    The Composite Interface (Abstract Component). \
    This Class may declaration of common methods that both \
    'Leafs' and 'Components' must implement.
    """

    @abstractmethod
    def show_details(self):
        """
        This method must be supported for both 'Leaf' and 'Composite' components.
        """
        ...


class File(FileSystemComponent):
    """
    This class represents a 'Leaf'. \
    This class may implement additional methods only for the 'Leaf'.
    """

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self):
        return f"{self.name} | {self.size}"


class Folder(FileSystemComponent):
    """
    This class represents the 'Composite'. \
    This class may implement additional methods for the 'Composite' that allows to manage its \
    children (e.g., add, remove, etc.).
    """

    def __init__(self, name):
        self.name = name
        self.children: FileSystemComponent = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def show_details(self):
        details = f"📁 Folder: {self.name}\n"

        for child in self.children:
            details += "|- " + child.show_details() + "\n"

        return details.strip()


# Client code
if __name__ == "__main__":
    file1 = File("resume.pdf", 200)
    file2 = File("photo.jng", 500)

    folder1 = Folder("Documents")
    folder1.add(file1)
    folder1.add(file2)

    subfolder = Folder("Projects")
    subfolder.add(File("project1.docx", 1300))
    folder1.add(subfolder)

    print(folder1.show_details())
