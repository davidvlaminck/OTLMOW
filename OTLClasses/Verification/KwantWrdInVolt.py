from ModelGenerator.BaseClasses.DecimalField import DecimalField


class KwantWrdInVolt:
    waarde = DecimalField()
    """Bevat een getal die bij het datatype hoort."""

    def __init__(self, waarde: DecimalField = None):
        self.waarde: DecimalField = waarde

    _standaardEenheid = "V"

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""
        return self._standaardEenheid