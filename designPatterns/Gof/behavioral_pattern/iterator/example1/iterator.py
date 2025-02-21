"""
This module implements the Iterator design pattern.
"""


from abc import ABC, abstractmethod


class Book:
    """
    This class represents a single element within a Collection (Aggregate)
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author}"


class Collection(ABC):
    """
    This class represents the Aggregate Interface.
    """

    @abstractmethod
    def add(self, element):
        ...

    @abstractmethod
    def create_iterator(self):
        ...


class Iterator(ABC):
    """
    This class represents the 'Iterator Interface' (or Abstract Iterator)
    """

    @abstractmethod
    def has_next(self) -> bool:
        ...

    @abstractmethod
    def next(self):
        ...


class BookIterator(Iterator):
    """
    This class represents the 'Concrete Iterator' associated with \
    the 'BookCollection'
    """

    def __init__(self, book_collection: Collection):
        self.book_collection = book_collection
        self.index = 0  # Keep track of the current position

    def has_next(self):
        return self.index < len(self.book_collection.books)

    def next(self):
        if self.has_next():
            book = self.book_collection.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


class BookCollection(Collection):
    """
    This class represents the 'Aggregate' (a Collection of elements)
    """

    def __init__(self):
        self.books = []

    def add(self, book: Book):
        self.books.append(book)

    def create_iterator(self):
        return BookIterator(self)


# Client code
if __name__ == "__main__":

    # 1. Create new element
    book1 = Book("Title1", "Sergei")
    book2 = Book("Title2", "Chabrov")

    # 2. Instantiate the Collection of elements
    aggregate = BookCollection()

    # 3. Add new element to the collection
    [aggregate.add(book) for book in [book1, book2]]

    # 4. Traverse through the collection

    # 4.1 Get the Iterator for an appropriate collection
    iterator = aggregate.create_iterator()

    # 4.2 Traverse
    while iterator.has_next():
        book = iterator.next()
        print(f"element='{iterator.index}', '{book}'")
