import os
import unittest

from OTLMOW.Facility.SettingsManager import SettingsManager

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SingletonTests(unittest.TestCase):
    def test_instantiate_settingsmanager(self):
        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/Facility/settings_sample.json'))
        id = None

        with self.subTest('instantiate settings manager'):
            settingsmanager = SettingsManager(settings_path=filelocation)
            self.assertEqual('OTLMOW', settingsmanager.settings['file_formats'][0]['name'])
            id = settingsmanager.__hash__()

        with self.subTest('instantiate settings manager again'):
            settingsmanager2 = SettingsManager(settings_path=filelocation)
            self.assertEqual(id, settingsmanager2.__hash__())
