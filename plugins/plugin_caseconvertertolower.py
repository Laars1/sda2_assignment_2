from common.plugin_base import Plugin
from core.core import *


class CaseConverterToLower(Plugin):
    def register(self, core):
        self.core = core
        core.register_plugin(self) # how to call this now?

    def execute(self, input: str, output: str):
        content = self.core.read_file(input)
        lower_content = self.core.to_lower(content)
        self.core.save_file(str(lower_content), output, self.name)

        log_message = f"{self.name}: Output is: {lower_content}"
        self.core.log(LogType.INFORMATION, log_message)

        return lower_content