from abc import ABC, abstractmethod


# Stage 1: Create Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        ...


class Window(ABC):
    @abstractmethod
    def render(self):
        ...


class AbstractGUIFactory(ABC):
    @abstractmethod
    def get_button(self) -> Button:
        ...

    @abstractmethod
    def get_window(self) -> Window:
        ...


# Stage 2: Create concrete classes.

# 2.1. Create concrete product classes

class WindowsButton(Button):
    def render(self):
        return "Windows button"


class WindowsWindow(Window):
    def render(self):
        return "Windows window"


class UbuntuButton(Button):
    def render(self):
        return "Ubuntu button"


class UbuntuWindow(Window):
    def render(self):
        return "Ubuntu window"


# 2.2. Create concrete factories.

class WindowsGUIFactory(AbstractGUIFactory):
    def get_button(self) -> Button:
        return WindowsButton()

    def get_window(self):
        return WindowsWindow()


class UbuntuFactory(AbstractGUIFactory):
    def get_button(self) -> Button:
        return UbuntuButton()

    def get_window(self):
        return UbuntuWindow()


# Client
def render_ui(factory: AbstractGUIFactory):
    button = factory.get_button()
    window = factory.get_window()

    print(button.render())
    print(window.render())


# Usage
if __name__ == "__main__":
    windows_factory = WindowsGUIFactory()
    ubuntu_factory = UbuntuFactory()

    render_ui(windows_factory)
    render_ui(ubuntu_factory)
