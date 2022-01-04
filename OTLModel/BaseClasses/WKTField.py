from shapely import wkt

from OTLModel.Datatypes.StringField import StringField


class WKTField(StringField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

# TODO wkt library is not loading
    def __setattr__(self, name, value):
        if type(self) == WKTField:
            if name == "waarde" and self.readonly and value is not None:
                raise AttributeError(f"can't set the value of a readonly attribute")
            if name == "waarde":
                if value is not None and not isinstance(value, str):
                    raise ValueError(f'expecting a string in {self.naam}')
                if value is not None:
                    try:
                        wkt.loads(value)
                    except:
                        raise ValueError(f'expecting a valid WKT string in {self.naam}')
            self.__dict__[name] = value
