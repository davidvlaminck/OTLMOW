from datetime import datetime

from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class DateField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(datetime, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly,
                         readonlyValue)

    def default(self):
        if self.waarde is not None:
            return self.waarde.strftime("%Y-%m-%d")
        return ''
