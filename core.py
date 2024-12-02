import logging
from common.log_type import LogType
import string


class CoreKernal:
    def read_file(self, path: string):
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            self.log(LogType.ERROR, "File not found")

    def save_file(self, content: string, path: string):
        try:
            with open(path, "w") as file:
                file.write(content)
                file.close()
                self.log(LogType.INFORMATION, "File saved in " + path)

        except FileNotFoundError:
            self.log(LogType.ERROR, "File not found at " + path)

    def to_lower(self, content: string):
        return content.lower()

    def to_upper(self, content: string):
        return content.upper()

    def log(self, type: LogType, content: string):
        if type == LogType.INFORMATION:
            logging.info(content)
        if type == LogType.WARNING:
            logging.warning(content)
        if type == LogType.INFORMATION:
            logging.error(content)
