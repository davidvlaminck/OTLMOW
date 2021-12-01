class KeuzelijstWaarde:
    def __init__(self, waarde, label, definitie, uri):
        self.waarde = waarde
        self.label = label
        self.definitie = definitie
        self.uri = uri


class KeuzelijstField:
    def __init__(self, naam, label, uri):
        self.naam = naam
        self.label = label
        self.uri = uri
        self.options = []

    def addOption(self, waarde, label, definitie, uri):
        self.options.append(KeuzelijstWaarde(waarde, label, definitie, uri))

    def getOptions(self):
        return self.options

    def getOptionByValue(self, waarde):
        return next(o for o in self.options if o.waarde == waarde)

    def getOptionByLabel(self, label):
        return next(o for o in self.options if o.label == label)
