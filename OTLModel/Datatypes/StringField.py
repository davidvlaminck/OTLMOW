from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class StringField(PrimitiveField):
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(str, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)
