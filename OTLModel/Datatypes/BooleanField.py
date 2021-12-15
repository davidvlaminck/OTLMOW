from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class BooleanField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version):
        super().__init__(bool, naam, label, uri, definition, constraints, usagenote, deprecated_version)




