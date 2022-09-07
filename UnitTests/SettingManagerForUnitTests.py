import platform


def get_settings_path_for_unittests():
    if platform.system() == 'Linux':
        return '/home/davidlinux/Documents/AWV/resources/settings_OTLMOW.json'
    else:
        return 'C:\\resources\\settings_OTLMOW.json'
