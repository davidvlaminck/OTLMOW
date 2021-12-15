from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class IntField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(int, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

