# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KlFormaatGebakkenStraatsteen import KlFormaatGebakkenStraatsteen
from OTLModel.Datatypes.KlStandaardkwaliteitsklasse import KlStandaardkwaliteitsklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGebakkenStraatsteen(Bestrating, AttributeInfo):
    """Gebakken straatstenen zijn straatstenen, in hoofdzaak vervaardigd uit klei al dan niet gemengd met leem, zand, brandstoffen of andere toeslagstoffen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Bestrating.__init__(self)

        self._formaatVanBestratingselement = OTLAttribuut(field=KlFormaatGebakkenStraatsteen,
                                                          naam='formaatVanBestratingselement',
                                                          label='formaat van bestratingselement',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.formaatVanBestratingselement',
                                                          definition='Bepaling van de afmeting van het bestratingselement.')

        self._standaardkwaliteitsklasse = OTLAttribuut(field=KlStandaardkwaliteitsklasse,
                                                       naam='standaardkwaliteitsklasse',
                                                       label='standaardkwaliteitsklasse',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.standaardkwaliteitsklasse',
                                                       definition='De standaardkwaliteitsklasse volgens PTV 910.')

    @property
    def formaatVanBestratingselement(self):
        """Bepaling van de afmeting van het bestratingselement."""
        return self._formaatVanBestratingselement.waarde

    @formaatVanBestratingselement.setter
    def formaatVanBestratingselement(self, value):
        self._formaatVanBestratingselement.set_waarde(value, owner=self)

    @property
    def standaardkwaliteitsklasse(self):
        """De standaardkwaliteitsklasse volgens PTV 910."""
        return self._standaardkwaliteitsklasse.waarde

    @standaardkwaliteitsklasse.setter
    def standaardkwaliteitsklasse(self, value):
        self._standaardkwaliteitsklasse.set_waarde(value, owner=self)
