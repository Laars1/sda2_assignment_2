from common.log_type import LogType
from common.plugin_base import Plugin
from transformers import pipeline


class Summary(Plugin):
    def register(self, core):
        self.core = core
        core.register_plugin(self)

    def execute(self, input: str, output: str):
        """
        Executes the summarization process on the input file and saves the summary to the output file.
        Args:
            input (str): The path to the input file containing the text to be summarized.
            output (str): The path to the output file where the summary will be saved.
        Returns:
            str: The generated summary of the input text.
        """
        content = self.core.read_file(input)

        summarizer = pipeline(
            "summarization",
            model="Falconsai/text_summarization",
            device="cpu",
            clean_up_tokenization_spaces=True,
        )  # Load ML model
        summary = summarizer(content, do_sample=False)
        self.core.save_file(str(summary), output, self.name)

        log_message = f"{self.name}: Generated summary from input: {summary}"
        self.core.log(LogType.INFORMATION, log_message)
        return summary