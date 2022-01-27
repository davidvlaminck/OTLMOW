from datetime import datetime

from src.OTLMOW.Facility.AbstractAttributeSetter import AbstractAttributeSetter


class DateFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = datetime.strptime(value, '%Y-%m-%d')