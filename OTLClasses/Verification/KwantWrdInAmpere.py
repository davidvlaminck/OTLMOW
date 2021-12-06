from ModelGenerator.BaseClasses.DecimalField import DecimalField


class KwantWrdInAmpere:
    """Een kwantitatieve waarde die een getal in ampère uitdrukt."""

    waarde = DecimalField()
    """Bevat een getal die bij het datatype hoort."""

    def __init__(self, waarde: DecimalField = None):
        self.waarde: DecimalField = waarde

    _standaardEenheid = "A"

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in ampere."""
        return self._standaardEenheid
