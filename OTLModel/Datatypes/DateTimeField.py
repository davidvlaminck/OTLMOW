from datetime import datetime

from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class DateTimeField(PrimitiveField):
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(datetime, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly,
                         readonlyValue)

    def default(self):
        return self.waarde.strftime("%Y-%m-%d %H:%M:%S")
