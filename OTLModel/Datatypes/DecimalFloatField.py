import decimal

from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class DecimalFloatField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version):
        super().__init__(float, naam, label, uri, definition, constraints, usagenote, deprecated_version)
