from OTLModel.Datatypes.StringField import StringField


class URIField(StringField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False,
                 readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

    # TODO add URI validation

