from abc import ABC, abstractmethod


# 1. Product

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None

    def __str__(self):
        return f"Computer(CPU: {self.cpu}, RAM: {self.ram}, GPU: {self.gpu}, Storage: {self.storage})"

# 2. Builder

# 2.1 Builder interface


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        ...

    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def set_ram(self, ram):
        ...

    @abstractmethod
    def set_gpu(self, gpu):
        ...

    @abstractmethod
    def set_storage(self, storage):
        ...

    @abstractmethod
    def build(self) -> Computer:
        ...

# 2.2 Concrete builders


class GamingPCBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

        return self

    def set_ram(self, ram):
        self.computer.ram = ram

        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu

        return self

    def set_storage(self, storage):
        self.computer.storage = storage

        return self

    def build(self):
        built_computer = self.computer
        self.reset()

        return built_computer

# 3. Director


class ComputerDirector:
    """Encapsulates the building process for predefined configurations."""

    # Predefined configuration 1

    @staticmethod
    def build_gaming_pc(builder: ComputerBuilder) -> Computer:
        return (
            builder
            .set_cpu("Intel i9")
            .set_ram("128GB")
            .set_gpu("NVIDIA RTX 4090")
            .set_storage("2TB SSD")
            .build()
        )

    # Predefined configuration 2

    @staticmethod
    def build_office_pc(builder: ComputerBuilder) -> Computer:
        return (
            builder
            .set_cpu("Intel i3")
            .set_ram("32GB")
            .set_gpu("Integrated Graphics")
            .set_storage("512TB SSD")
            .build()
        )


# 4. Client

def build_computers():
    builder = GamingPCBuilder()

    gaming_pc = ComputerDirector.build_gaming_pc(builder)
    office_pc = ComputerDirector.build_office_pc(builder)

    print(gaming_pc)
    print(office_pc)


# Use
if __name__ == "__main__":
    build_computers()
