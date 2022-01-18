class OTLField:
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        raise SyntaxError('')
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.definition = definition
        self.constraints = constraints
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version
        self.readonly = readonly
        self.readonlyValue = None
        self.waarde = None
        if readonly:
            self.__dict__["waarde"] = readonlyValue

    @staticmethod
    def default(value):
        return value.waarde
