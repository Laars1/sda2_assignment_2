from typing import Counter
from common.plugin_base import Plugin
from core import *


class WordCounter(Plugin):
    def execute(self, input, output):
        content = self.core.read_file(input)

        word_count = len(content.split())

        self.core.save_file(str(word_count), output, self.name)

        log_message = "WordCounter: file from path",input,"conatins",str(word_count),"words"
        self.core.log(LogType.INFORMATION, log_message)
        return word_count