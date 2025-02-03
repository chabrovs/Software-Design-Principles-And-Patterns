from abc import ABC, abstractmethod


# Abstract class (contract)
class Plugin(ABC):
    @abstractmethod
    def execute(self):
        ...


# Concrete implementation
class EmailPlugin(Plugin):
    def execute(self):
        print("Sending an Email...")


class SMSPlugin(Plugin):
    def execute(self):
        print("Sending SMS...")


# This class is responsible for flow control of the entire program.
class Framework:
    def run_plugin(self, plugin: Plugin):
        print(f"Framework executing plugin {plugin}")
        plugin.execute()


if __name__ == "__main__":
    framework = Framework()
    plugin = SMSPlugin()

    framework.run_plugin(plugin)

    plugin = EmailPlugin()

    framework.run_plugin(plugin)


# The Framework class (higher-level component) decides when to call the plugins \
# (lower-level components).
# Lower-level components on;y implement the behavior and do not control the flow.  