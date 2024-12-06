from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Abstract base class for creating plugins. Each plugin must implement the
    `register` method to register itself with the core and the `execute` method
    to define its functionality.

    Attributes:
        name (str): The name of the plugin, which is automatically set based on 
                    the class name.
    """
    
    def __init__(self):
        self.name = self.__class__.__name__


    @abstractmethod
    def register(self, core):
        """
        Register the plugin with the given core.
        """
        pass

    @abstractmethod
    def execute(self, input: str, output: str):
        """
        Execute the plugin with the given input and output.
        """
        pass
