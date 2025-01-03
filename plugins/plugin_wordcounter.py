from common.plugin_base import Plugin
from core.core import *


class WordCounter(Plugin):
    def register(self, core):
        self.core = core
        core.register_plugin(self)

    def execute(self, input: str, output: str) -> int:
        """
        Executes the word counting process on the given input file and saves the result to the output file.
        Args:
            input (str): The path to the input file to be processed.
            output (str): The path to the output file where the word count will be saved.
        Returns:
            int: The number of words in the input file.
        Logs:
            Logs an informational message with the word count of the input file.
        """
        content = self.core.read_file(input)

        word_count = len(content.split())

        self.core.save_file(str(word_count), output, self.name)

        log_message = f"{self.name}: file from path {input} contains {word_count} words"
        self.core.log(LogType.INFORMATION, log_message)

        return word_count