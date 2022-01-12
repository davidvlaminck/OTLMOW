from datetime import time

from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class TimeField(PrimitiveField):
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(time, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

    def default(self):
        return self.waarde.strftime("%H:%M:%S")
