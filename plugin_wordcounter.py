from typing import Counter
from common.plugin_base import Plugin
from core import *


class WordCounter(Plugin):
    def execute(self, input):
        content = self.core.read_file(input)

        content = self.core.to_lower(content)

        words = content.split()

        word_count = Counter(words).most_common(10)
        self.core.log(LogType.INFORMATION, "Generated most common words from given input:" + str(word_count))
        return word_count