from shapely import wkt
from shapely.errors import WKTReadingError

from OTLModel.Datatypes.StringField import StringField


class WKTField(StringField):
    def __init__(self, naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(naam, label, objectUri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

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
                    except WKTReadingError as error:
                        raise ValueError(f'{value} is not a valid WKT string for {self.naam}: {str(error)}')
            self.__dict__[name] = value
