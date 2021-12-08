from abc import abstractmethod


class OTLField:
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        self.naam = naam
        self.label = label
        self.uri = uri
        self.definition = definition
        self.constraints = constraints
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version
        self.readonly = readonly
        self.waarde = None
        if readonly:
            self.__dict__["waarde"] = readonlyValue

    def __set__(self, instance, value):
        raise SyntaxError("You can not set this field with assignment. Use .waarde instead.")
