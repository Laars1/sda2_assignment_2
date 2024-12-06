from core.core import CoreKernal
from plugins.plugin_summary import Summary
from plugins.plugin_topkeywords import TopKeyWords
from plugins.plugin_wordcounter import WordCounter

default_input = "test.txt"
default_output = "output.txt"

core = CoreKernal()


chosen_plugin = input("Choose a plugin (Enter name of Plugin, if you want to extcute all - type ALL): ")
try:
    if chosen_plugin == "ALL":
        core.execute_plugins(default_input, default_output)
    else:
        # Process the input file using the selected plugin and wriALLte to the output file
        core.execute_plugin(chosen_plugin, default_input, default_output)
    
except Exception as e:
    print(f"Error: {e}")
