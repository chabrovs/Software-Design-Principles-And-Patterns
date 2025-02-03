from abc import ABC, abstractmethod
from typing import List


class Plugin(ABC):
    @abstractmethod
    def execute(self):
        ...


class PrintPlugin(Plugin):
    def execute(self):
        print("Executing print plugin.")


class ScanPlugin(Plugin):
    def execute(self):
        print("Execution scan plugin. ")


if __name__ == "__main__":
    # Dynamically load plugins. 
    enabled_plugin_list: List[Plugin] = [PrintPlugin(), ScanPlugin()]
    for plugin in enabled_plugin_list:
        plugin.execute()


# This module adheres the OCP because \
# it enables adding new functionality by adding new plugins \
# that are distinct classes from the app, or other plugins \
# thus the code modification in not required.  