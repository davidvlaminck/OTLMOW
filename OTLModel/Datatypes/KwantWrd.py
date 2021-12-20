from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.OTLField import OTLField
from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class KwantWrd(OTLField):
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, waardeVeld: PrimitiveField,
                 eenheidVeld, readonly=False, readonlyValue=None, waarde=None):
        self.waardeVeld = waardeVeld
        if not(eenheidVeld is None or isinstance(eenheidVeld, LiteralField)):
            raise TypeError("eenheidVeld is not the correct fieldType (LiteralField or None)")
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

    def default(self):
        return self.waardeVeld.waarde
