from core import CoreKernal
from plugin_wordcounter import WordCounter


core = CoreKernal()
plugin_wordcounter = WordCounter(core)

path = "test.txt"

print("Word Counter:", str(plugin_wordcounter.execute(path)))