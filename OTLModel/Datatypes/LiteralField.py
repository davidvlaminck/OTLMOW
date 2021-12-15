from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class LiteralField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonlyValue=None):
        super().__init__(str, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=True,
                         readonlyValue=readonlyValue)
