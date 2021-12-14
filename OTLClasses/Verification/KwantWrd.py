from ModelGenerator.BaseClasses.ComplexField import ComplexField
from ModelGenerator.BaseClasses.LiteralField import LiteralField
from ModelGenerator.BaseClasses.OTLField import OTLField
from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class KwantWrd(OTLField):
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, waardeVeld: PrimitiveField,
                 eenheidVeld: LiteralField, readonly=False, readonlyValue=None, waarde=None):
        self.waardeVeld = waardeVeld
        self.eenheidVeld = eenheidVeld
        super().__init__(naam, label, uri, definition, usagenote, deprecated_version, readonly,
                         readonlyValue)
        if waarde is not None:
            self.waarde = waarde

    def __setattr__(self, key, value):
        if key == "waarde":
            self.waardeVeld.waarde = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, name):
        if name == "waarde":
            return self.waardeVeld.waarde
        else:
            return object.__getattribute__(self, name)

