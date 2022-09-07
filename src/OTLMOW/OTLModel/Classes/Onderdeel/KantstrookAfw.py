# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class KantstrookAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, bestemd om de verharding steun te geven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandAfw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd')

        self._aantalRijenBetonstraatsteen = OTLAttribuut(field=IntegerField,
                                                         naam='aantalRijenBetonstraatsteen',
                                                         label='aantal rijen betonstraatsteen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw.aantalRijenBetonstraatsteen',
                                                         definition='Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd.',
                                                         owner=self)

    @property
    def aantalRijenBetonstraatsteen(self):
        """Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd."""
        return self._aantalRijenBetonstraatsteen.get_waarde()

    @aantalRijenBetonstraatsteen.setter
    def aantalRijenBetonstraatsteen(self, value):
        self._aantalRijenBetonstraatsteen.set_waarde(value, owner=self)
