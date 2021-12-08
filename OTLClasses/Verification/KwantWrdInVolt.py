from ModelGenerator.BaseClasses.DecimalField import DecimalField
from ModelGenerator.BaseClasses.StringField import StringField


class KwantWrd:
    def __setattr__(self, key, value):
        if key == "waarde":
            self.waarde.waarde = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, name):
        if name == "waarde":
            return self.waarde.waarde
        else:
            return object.__getattribute__(self, name)

    def __init__(self, waarde=None):
        if waarde is not None:
            self.waarde = waarde


class KwantWrdInVolt(KwantWrd):
    waarde = DecimalField(naam="waarde", label="waarde",
                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde",
                          definition="Bevat een getal die bij het datatype hoort."
                          , constraints="", usagenote="", deprecated_version="")
    """Bevat een getal die bij het datatype hoort."""

    standaardEenheid = StringField(naam="standaardEenheid", label="standaardEenheid",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid",
                                   definition="De standaard eenheid bij dit datatype is uitgedrukt in Volt."
                                   , constraints="", usagenote="", deprecated_version="", readonly=True, readonlyValue="V")
    """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""


