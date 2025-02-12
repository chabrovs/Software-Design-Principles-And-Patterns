"""
The Virtual Proxy allows to initiated an object only when it it \
required, instead of initiating at the time the program loads.
"""


from time import sleep


class ExpensiveObject:
    def __init__(self):
        print("Loading an expensive object...")
        sleep(3)

    def process(self):
        return "Data"


# Proxy class (Lazy initialization)
class VirtualProxy:
    """
    The 'VirtualProxy' class should implement the same interface \
    as the 'ExpensiveObject' class.
    """

    def __init__(self):
        self._real_object = None

    def process(self):
        if not self._real_object:
            self._real_object = ExpensiveObject()

        return self._real_object.process()


# Client code
if __name__ == "__main__":
    proxy = VirtualProxy()
    # If the 'process' never call the 'ExpensiveObject' will never be initialized.
    print(proxy.process())
