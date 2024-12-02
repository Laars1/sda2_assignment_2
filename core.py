import logging
from common.log_type import LogType
import string


class CoreKernal:
    def read_file(self, path: string):
        # TODO: Implement Method
        return ""

    def save_file(self, content: string):
        # TODO: Implement Method
        return ""
    
    def to_lower(self, content: string):
        # TODO: Implement Method
        return ""
    
    def to_upper(self, content: string):
        # TODO: Implement Method
        return ""
    
    def log(self, type: LogType, content: string):
        if type == LogType.INFORMATION:
            logging.info(content)
        if type == LogType.WARNING:
            logging.warning(content)
        if type == LogType.INFORMATION:
            logging.error(content)