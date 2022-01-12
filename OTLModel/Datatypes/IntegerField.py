from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class IntegerField(PrimitiveField):
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(int, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

