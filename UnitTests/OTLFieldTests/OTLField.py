from abc import abstractmethod


class OTLField:
    _uses_waarde_object = False
    naam = ''
    label = ''
    objectUri = ''
    definition = ''
    usagenote = ''
    deprecated_version = ''
    waardeObject = None

    @staticmethod
    def validate(value, attribuut):
        pass

    @staticmethod
    def convert_to_correct_type(value):
        return value

    @abstractmethod
    def __str__(self):
        return f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""
