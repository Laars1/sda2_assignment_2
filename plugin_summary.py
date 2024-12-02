import string
from common.log_type import LogType
from common.plugin_base import Plugin
from transformers import pipeline


class Summary(Plugin):
    def execute(self, input: string, output: string):
        content = self.core.read_file(input)

        words_count = int(len(content.split()))
        min_lenth = round(words_count / 10)
        max_lenth = round(words_count / 2)

        summarizer = pipeline("summarization", model="Falconsai/text_summarization", device=0) # load ML model
        summary = summarizer(content, max_length=max_lenth, min_length=min_lenth, do_sample=False)
        self.core.save_file(str(summary), output, self.name)

        log_message = "Summary: Generated summary from inout" + str(summary)
        self.core.log(LogType.INFORMATION, log_message)
        return summary