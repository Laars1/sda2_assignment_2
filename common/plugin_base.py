from abc import ABC, abstractmethod
import string


class Plugin(ABC):
    def __init__(self):
        # self.core = core
        self.name = self.__class__.__name__

    """
    Register the plugin with the given core.
    """

    @abstractmethod
    def register(self, core):
        pass

    """
    Execute the plugin with the given input and output.
    """

    @abstractmethod
    def execute(self, input: string, output: string):
        pass
