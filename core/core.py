from pathlib import Path
from common.log_type import LogType
import string

from plugins.plugin_summary import Summary
from plugins.plugin_topkeywords import TopKeyWords
from plugins.plugin_wordcounter import WordCounter


class CoreKernal:
    log_level = LogType.INFORMATION

    def __init__(self, log_level=None):
            if log_level:
                self.log_level = log_level

            self._plugins = []
            
            logging_plugin = TopKeyWords()
            security_plugin = WordCounter()
            summary_plugin = Summary()

            # Plugins register themselves with the core
            logging_plugin.register(self)
            security_plugin.register(self)
            summary_plugin.register(self)

    def register_plugin(self, plugin):
            self._plugins.append(plugin)
            print(f"Plugin {plugin.__class__.__name__} registered.")

    def execute_plugins(self, input: string, output: string):
        for plugin in self._plugins:
            print(f"Executing plugin: {plugin.__class__.__name__}")
            plugin.execute(input, output)
        
    def execute_plugin(self, plugin_name: str, input: str, output: str):
        for plugin in self._plugins:
            if plugin.__class__.__name__ == plugin_name:
                print(f"Executing plugin: {plugin_name}")
                plugin.execute(input, output)
                return
        print(f"Plugin {plugin_name} not found.")

    def read_file(self, path: string):
        """
        Reads the content of a file specified by the given path.

        Args:
            path (str): The path to the file to be read.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist at the specified path.
        """
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            self.log(LogType.ERROR, "File not found")

    def save_file(self, content: string, path: string, className: string):
        """
        Saves the given content to a file at the specified path, appending the content
        to the file if it already exists.

        Args:
            content (str): The content to be written to the file.
            path (str): The path where the file will be saved.
            className (str): The name of the class to be included in the file content.

        Raises:
            FileNotFoundError: If the file at the specified path cannot be found.

        Logs:
            Logs an informational message when the file is successfully saved.
            Logs an error message if the file cannot be found.
        """
        try:
            with open(path, "a+") as file:
                file.write(f"{className}:\n{content}\n\n")
            self.log(LogType.DEBUG, f"File saved in {path}")
        except FileNotFoundError:
            self.log(LogType.ERROR, f"File not found at {path}")

    def to_lower(self, content: string):
        return content.lower()

    def to_upper(self, content: string):
        return content.upper()

    def log(self, type: LogType, content: string):
        """
        Logs a message with a specified log type.
        Logs only message which are selected in within the log_level

        Args:
            type (LogType): The type of log message (INFORMATION, WARNING, ERROR, DEBUG).
            content (str): The content of the log message.

        Returns:
            None
        """

        log_levels = {
            LogType.INFORMATION: 1,
            LogType.WARNING: 2,
            LogType.ERROR: 3,
            LogType.DEBUG: 0,
        }

        if log_levels[type] >= log_levels[self.log_level]:
            print(f"{type}: {content}")