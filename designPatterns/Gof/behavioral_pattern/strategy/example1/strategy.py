"""

"""

from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    """
    This class represents the 'Strategy Interface (or Abstract Strategy)'
    """

    @abstractmethod
    def sort(self, data):
        ...


class DefaultSort(SortingStrategy):
    """
    This class represents a 'Concrete Strategy'
    """

    def sort(self, data):
        return sorted(data)


class BubbleSort(SortingStrategy):
    """
    This class represents a 'Concrete Strategy'
    """

    def sort(self, data):
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        return data


class Sorter:
    """
    This class represents the 'Context (or Main object)'
    """

    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)


# Client code

if __name__ == "__main__":
    sorter = Sorter(BubbleSort())
    print(sorter.sort_data([3, 2, 1]))
