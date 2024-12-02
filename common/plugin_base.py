from abc import ABC, abstractmethod
import string


class Plugin(ABC):
    def __init__(self, core):
        self.core = core
        self.name = self.__class__.__name__
 
    @abstractmethod
    def execute(self, input: string, output: string):
        pass