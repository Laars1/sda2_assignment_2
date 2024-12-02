from typing import Counter
from common.log_type import LogType
from common.plugin_base import Plugin


class TopKeyWords(Plugin):
    def execute(self, input, output):
        content = self.core.read_file(input)
        content = self.core.to_lower(content)

        words = content.split()

        most_common = Counter(words).most_common(10)

        self.core.save_file(str(most_common), output, self.name)

        log_message = "TopKeyWords: Most common words from given input:" + str(most_common)
        self.core.log(LogType.INFORMATION, log_message)
        return most_common