from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class IntField(PrimitiveField):
    def __init__(self, uri: str):
        self.uri = uri
        super().__init__(int)

