# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting
from src.OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalRijenBetonstraatsteen = OTLAttribuut(field=IntegerField,
                                                         naam='aantalRijenBetonstraatsteen',
                                                         label='aantal rijen betonstraatsteen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelAfw.aantalRijenBetonstraatsteen',
                                                         definition='Het aantal rijen betonstraatsteen waaruit de watergreppel is opgebouwd.')

    @property
    def aantalRijenBetonstraatsteen(self):
        """Het aantal rijen betonstraatsteen waaruit de watergreppel is opgebouwd."""
        return self._aantalRijenBetonstraatsteen.waarde

    @aantalRijenBetonstraatsteen.setter
    def aantalRijenBetonstraatsteen(self, value):
        self._aantalRijenBetonstraatsteen.set_waarde(value, owner=self)
