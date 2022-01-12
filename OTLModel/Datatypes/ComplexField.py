from OTLModel.Datatypes.OTLField import OTLField


class ComplexAttributen:
    def default(self):
        d = {}
        for k, v in self.__dict__.items():
            if v.default() is not None:
                d[k] = v.default()
        return d


class ComplexField(OTLField):
    def __init__(self, naam, label, objectUri, definition, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(naam=naam, label=label, objectUri=objectUri, definition=definition, constraints=None,
                         usagenote=usagenote, deprecated_version=deprecated_version, readonly=readonly,
                         readonlyValue=readonlyValue)
        self.waarde = ComplexAttributen()

    def default(self):
        return self.waarde.default()
