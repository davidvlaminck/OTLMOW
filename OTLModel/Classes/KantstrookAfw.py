# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting
from OTLModel.Datatypes.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class KantstrookAfw(AfwijkendeKantopsluiting, AttributeInfo):
    """Afwijkende kantopsluiting, bestemd om de verharding steun te geven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfwijkendeKantopsluiting.__init__(self)
        AttributeInfo.__init__(self)

        self._aantalRijenBetonstraatsteen = OTLAttribuut(field=IntegerField,
                                                         naam='aantalRijenBetonstraatsteen',
                                                         label='aantal rijen betonstraatsteen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw.aantalRijenBetonstraatsteen',
                                                         definition='Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd.')

    @property
    def aantalRijenBetonstraatsteen(self):
        """Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd."""
        return self._aantalRijenBetonstraatsteen.waarde

    @aantalRijenBetonstraatsteen.setter
    def aantalRijenBetonstraatsteen(self, value):
        self._aantalRijenBetonstraatsteen.set_waarde(value, owner=self)
