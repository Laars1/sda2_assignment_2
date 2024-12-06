import importlib
import pkgutil
from common.plugin_base import Plugin
from core.core import CoreKernal
        
if __name__ == '__main__':
    # To enable detailed logging, instantiate the CoreKernal with the desired log level. Default is LogType.INFORMATION
    # Example: CoreKernal(log_level=LogType.DEBUG) will show debug-level logs and above.
    core = CoreKernal()
    core.run()