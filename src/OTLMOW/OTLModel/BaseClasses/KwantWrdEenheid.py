from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo


class KwantWrdEenheid(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = None

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    def __str__(self):
        return f"""\n\ninformation about {self._standaardEenheid.naam}:
    naam: {self._standaardEenheid.naam}
    uri: {self._standaardEenheid.objectUri}
    definition: {self._standaardEenheid.definition}
    label: {self._standaardEenheid.label}
    usagenote: {self._standaardEenheid.usagenote}
    constraints: {self._standaardEenheid.constraints}
    deprecated_version: {self._standaardEenheid.deprecated_version}"""
