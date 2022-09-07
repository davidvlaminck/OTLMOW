import platform
from pathlib import Path


def get_settings_path_for_unittests():
    if platform.system() == 'Linux':
        return Path('/home/davidlinux/Documents/AWV/resources/settings_OTLMOW.json')
    else:
        return Path('C:\\resources\\settings_OTLMOW.json')
