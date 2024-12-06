from abc import ABC, abstractmethod
import string


class Plugin(ABC):
    def __init__(self):
        # self.core = core
        self.name = self.__class__.__name__


    @abstractmethod
    def register(self, core):
        """
        Register the plugin with the given core.
        """
        pass

    @abstractmethod
    def execute(self, input: string, output: string):
        """
        Execute the plugin with the given input and output.
        """
        pass
