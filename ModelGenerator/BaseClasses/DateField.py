from datetime import datetime

from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class DateField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(datetime, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

