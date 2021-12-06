from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class BooleanField(PrimitiveField):
    def __init__(self, uri: str):
        self.uri = uri
        super().__init__(bool)
