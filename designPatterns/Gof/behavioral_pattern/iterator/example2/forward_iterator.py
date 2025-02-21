"""
This module implements the Iterator design pattern utilizing Python built-in \
tools. 
"""

from collections.abc import Iterable, Iterator


class ListIterator(Iterator):
    """
    This class represents the 'Concrete Iterator'
    """

    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def __next__(self):
        """
        This special method allows to use special Python syntax for \
        interactions with with the 'Aggregate (Collection)' 
        """

        if not self.has_next():
            raise StopIteration

        value = self._collection[self._index]
        self._index += 1

        return value


class CustomList(Iterable):
    """
    This class represents an 'Aggregate (Collection)'
    """

    def __init__(self, items):
        self._items = items

    def __iter__(self):
        """
        This method returns a 'Concrete Iterator' associates with \
        the 'Aggregate'
        """

        return ListIterator(self._items)


# Client code
if __name__ == "__main__":
    my_list = CustomList(["I", "adore", "Python"])

    for item in my_list:  # This syntax automatically creates an iterator and traverses.
        print(item)
