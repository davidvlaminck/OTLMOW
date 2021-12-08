from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class IntField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version):
        super().__init__(int, naam, label, uri, definition, constraints, usagenote, deprecated_version)

