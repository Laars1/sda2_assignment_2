from typing import Counter
from common.plugin_base import Plugin
from core.core import *


class CaseConverterToUpper(Plugin):
    def register(self, core):
        self.core = core
        core.register_plugin(self)

    def execute(self, input, output):
        content = self.core.read_file(input)

        upper_content = self.core.to_upper(content)
        self.core.save_file(str(upper_content), output, self.name)

        log_message = "CaseConverterToUpper: Output is:" + str(
            upper_content
        )
        self.core.log(LogType.INFORMATION, log_message)
        return upper_content
