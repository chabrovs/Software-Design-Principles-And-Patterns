# Example: Button click GUI


from typing import Callable


class Button:
    def __init__(self):
        self.on_click: Callable | None = None

    def click(self):
        if self.on_click:
            self.on_click()


def handle_click():
    print("Button clicked!")


if __name__ == "__main__":
    button = Button()

    button.on_click = handle_click

    button.click()

# The 'Button' class is a higher-level component and the 'handle_click' function \
# is a lower-level component. The function is invoked when the higher-level component \
# calls for it. 