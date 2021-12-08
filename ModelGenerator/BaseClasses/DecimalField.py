import decimal

from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class DecimalField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version):
        super().__init__(decimal.Decimal, naam, label, uri, definition, constraints, usagenote, deprecated_version)

