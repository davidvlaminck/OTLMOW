import json

from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.Facility.Singleton import Singleton


class SettingsManager(metaclass=Singleton):
    def __init__(self, settings_path: str = ''):
        self.settings: dict = {}
        if settings_path != '':
            self.load_settings_from_file(settings_path)

    def load_settings_from_file(self, settings_path):
        with open(settings_path) as settings_file:
            self.settings = json.load(settings_file)
        if self.settings is not None:
            self.load_settings_in_app()

    def load_settings_in_app(self):
        if 'file_formats' in self.settings:
            otlmow_format = next((f for f in self.settings['file_formats'] if f['name'] == 'OTLMOW'), None)
            if otlmow_format is not None and 'dotnotatie' in otlmow_format:
                if 'separator' in otlmow_format['dotnotatie']:
                    DotnotatieHelper.separator = otlmow_format['dotnotatie']['separator']
                if 'cardinality separator' in otlmow_format['dotnotatie']:
                    DotnotatieHelper.cardinality_separator = otlmow_format['dotnotatie']['cardinality separator']
                if 'cardinality indicator' in otlmow_format['dotnotatie']:
                    DotnotatieHelper.cardinality_indicator = otlmow_format['dotnotatie']['cardinality indicator']
