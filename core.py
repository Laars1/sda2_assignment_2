import logging
from pathlib import Path
from common.log_type import LogType
import string


class CoreKernal:
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
            self.log(LogType.INFORMATION, f"File saved in {path}")
        except FileNotFoundError:
            self.log(LogType.ERROR, f"File not found at {path}")

    def to_lower(self, content: string):
        return content.lower()

    def to_upper(self, content: string):
        return content.upper()

    def log(self, type: LogType, content: string):
        """
        Logs a message with a specified log type.

        Args:
            type (LogType): The type of log message (INFORMATION, WARNING, ERROR).
            content (str): The content of the log message.

        Returns:
            None
        """
        if type == LogType.INFORMATION:
            logging.info(content)
        if type == LogType.WARNING:
            logging.warning(content)
        if type == LogType.ERROR:
            logging.error(content)
