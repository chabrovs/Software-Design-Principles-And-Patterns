"""
This module implements the Iterator design pattern utilizing Python built-in \
tools. 
"""


from collections.abc import Iterator, Iterable


class ListIterator(Iterator):
    """
    This class represents a 'Concrete Iterator'
    """

    def __init__(self, collection):
        self._collection = collection
        self._index = -1

    def has_next(self):
        return abs(self._index) <= len(self._collection)
    
    def __next__(self):
        if not self.has_next():
            raise StopIteration
        
        item = self._collection[self._index]
        self._index -= 1
    
        return item
    
class CustomList(Iterable):
    """
    This class represents the 'Aggregate (Collection)'
    """

    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return ListIterator(self._items)
    

# Client code
if __name__ == "__main__":
    aggregate = CustomList(["I", "adore", "Python"])

    for item in aggregate:
        print(item)