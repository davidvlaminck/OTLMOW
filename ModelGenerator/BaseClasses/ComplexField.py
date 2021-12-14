from ModelGenerator.BaseClasses.OTLField import OTLField


class ComplexAttributen:
    def default(self):
        d = {}
        for k, v in self.__dict__.items():
            d[k] = v.default()
        return d


class ComplexField(OTLField):
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(naam=naam, label=label, uri=uri, definition=definition, constraints=None, usagenote=usagenote,
                         deprecated_version=deprecated_version, readonly=readonly, readonlyValue=readonlyValue)
        self.waarde = ComplexAttributen()

    def default(self):
        return self.waarde.default()

