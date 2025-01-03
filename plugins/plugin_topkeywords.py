from typing import Counter, List, Tuple
from common.log_type import LogType
from common.plugin_base import Plugin


class TopKeyWords(Plugin):
    def register(self, core):
        self.core = core
        core.register_plugin(self)

    def execute(self, input: str, output: str) -> List[Tuple[str, int]]:
        """
        Executes the top keywords extraction process.
        Reads content from the input file, converts it to lowercase,
        splits it into words, counts occurrences, and identifies the
        top 10 most common words. The result is saved to the output file and logged.

        Args:
            input (str): The path to the input file.
            output (str): The path to the output file.

        Returns:
            list: A list of tuples containing the top 10 most common words and their counts.
        """
        content = self.core.read_file(input)
        content = self.core.to_lower(content)

        words = content.split()

        most_common = Counter(words).most_common(10)

        self.core.save_file(str(most_common), output, self.name)

        log_message = f"{self.name}: Most common words from given input: {most_common}"
        self.core.log(LogType.INFORMATION, log_message)

        return most_common