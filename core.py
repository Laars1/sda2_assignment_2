import logging
from pathlib import Path
from common.log_type import LogType
import string


class CoreKernal:
    def read_file(self, path: string):
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            self.log(LogType.ERROR, "File not found")

    def save_file(self, content: string, path: string, className: string):
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
        if type == LogType.INFORMATION:
            logging.info(content)
        if type == LogType.WARNING:
            logging.warning(content)
        if type == LogType.ERROR:
            logging.error(content)
