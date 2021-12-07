from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class StringField(PrimitiveField):
    def __init__(self):
        super().__init__(str)

