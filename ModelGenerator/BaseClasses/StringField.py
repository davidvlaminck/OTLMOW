from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class StringField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(str, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

