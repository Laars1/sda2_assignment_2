from abc import ABC, abstractmethod


class Plugin(ABC):
    def __init__(self, core):
        self.core = core
 
    @abstractmethod
    def execute(self, text):
        pass