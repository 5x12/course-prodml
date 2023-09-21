import os
import logging
from dynaconf import Dynaconf

# specifying logging level
logging.basicConfig(level=logging.INFO)

current_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    settings_files=f'{current_directory}\setting.toml'
)