﻿from OTLMOW.Facility.AbstractAttributeSetter import AbstractAttributeSetter


class KeuzelijstFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = value