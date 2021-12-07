from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class IntField(PrimitiveField):
    def __init__(self):
        super().__init__(int)

