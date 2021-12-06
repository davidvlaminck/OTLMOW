import decimal

from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class DecimalField(PrimitiveField):
    def __init__(self):
        super().__init__(decimal.Decimal)

