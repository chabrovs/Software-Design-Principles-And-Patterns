"""
A Prototype registry is useful when there are multiple \
prototypes needed to be managed efficiently.
"""


import copy


class PrototypeRegistry:
    """Manage a registry of Prototypes."""

    def __init__(self):
        self._prototype_registry = {}

    def register_prototype(self, key, prototype):
        self._prototype_registry[key] = prototype

    def get_prototype(self, key):
        return copy.deepcopy(self._prototype_registry.get(key))


class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Document(Title: '{self.title}', Content: '{self.content}')"


if __name__ == "__main__":
    registry = PrototypeRegistry()

    # Register prototype
    doc1 = Document("Report1", "This is report # 1.")
    registry.register_prototype("Report1", doc1)

    # Cloning prototype
    doc2 = registry.get_prototype("Report1")
    doc2.content = "This is Prototype"

    print(doc1)
    print(doc2)
