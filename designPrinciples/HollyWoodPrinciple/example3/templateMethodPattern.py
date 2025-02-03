# Example: Data processing pipeline

from abc import ABC, abstractmethod


class DataProcessorI(ABC):
    def process(self):
        # Method within an interface that has the control flow.
        self.read_data()
        self.transform_data()
        self.save_data()
    
    @abstractmethod
    def read_data(self):
        ...

    @abstractmethod
    def transform_data(self):
        ...

    @abstractmethod
    def save_data(self):
        ...

    
class CSVProcessor(DataProcessorI):
    def read_data(self):
        # Concrete implementation 
        print("Reding csv data...")

    def transform_data(self):
        # Concrete implementation 
        print("Transforming csv data...")
    
    def save_data(self):
        # Concrete implementation 
        print("Saving csv data...")


if __name__ == "__main__":
    processor = CSVProcessor()
    processor.process()


# The 'process'method within the 'DataProcessor' interface defines the overall flow, \
# and subclasses provide specific implementation. 

    