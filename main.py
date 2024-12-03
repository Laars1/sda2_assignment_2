from core import CoreKernal
from plugin_summary import Summary
from plugin_topkeywords import TopKeyWords
from plugin_wordcounter import WordCounter


core = CoreKernal()
plugin_wordcounter = WordCounter(core)
plugin_topkeywords = TopKeyWords(core)
plugin_summary = Summary(core)

path = "test.txt"

print("plugin_wordcounter:", str(plugin_wordcounter.execute(path, "output.txt"))) 
print("plugin_topkeywords:", str(plugin_topkeywords.execute(path, "output.txt")))
print("plugin_summary:", str(plugin_summary.execute(path, "output.txt")))