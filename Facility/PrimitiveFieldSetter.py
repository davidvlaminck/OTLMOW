from Facility.AbstractAttributeSetter import AbstractAttributeSetter


class PrimitiveFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = value