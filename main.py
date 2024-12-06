from core.core import CoreKernal
from plugins.plugin_summary import Summary
from plugins.plugin_topkeywords import TopKeyWords
from plugins.plugin_wordcounter import WordCounter


# core = CoreKernal()
# plugin_wordcounter = WordCounter(core)
# plugin_topkeywords = TopKeyWords(core)
# plugin_summary = Summary(core)

# path = "test.txt"

# print("plugin_wordcounter:", str(plugin_wordcounter.execute(path, "output.txt"))) 
# print("plugin_topkeywords:", str(plugin_topkeywords.execute(path, "output.txt")))
# print("plugin_summary:", str(plugin_summary.execute(path, "output.txt")))

default_input = "test.txt"
defult_output = "output.txt"

core = CoreKernal()

# Create plugins
logging_plugin = TopKeyWords()
security_plugin = WordCounter()

# Plugins register themselves with the core
logging_plugin.register(core)
security_plugin.register(core)

chosen_plugin = input("Choose a plugin: ")
try:
    # Process the input file using the selected plugin and write to the output file
    core.execute_plugin(chosen_plugin, default_input, defult_output)
    
except Exception as e:
    print(f"Error: {e}")
