# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.VRIDraagconstructie import VRIDraagconstructie
from OTLMOW.OTLModel.Datatypes.KlBoogpaalType import KlBoogpaalType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BoogpaalVerkeerslicht(VRIDraagconstructie, PuntGeometrie):
    """Paal bestemd voor het bevestigen van seinlantaarns boven het wegdek. Geschikt voor het bevestigen van ten hoogste 4 seinlantaarns van het type 300 en van één of meerdere lantaarns van het type 200 op de paalschacht. De vrije hoogte ten opzichte van het wegdek bedraagt onder de lantaarns 6.500 millimeter voor palen met grote draagwijdte (7,5 meter overspanning) en 5.500 millimeter voor de palen met middelgrote draagwijdte (3,5 meter overspanning)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VRIDraagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self._typeBoogpaal = OTLAttribuut(field=KlBoogpaalType,
                                          naam='typeBoogpaal',
                                          label='type boogpaal',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht.typeBoogpaal',
                                          definition='Draagwijdte van de boogpaal.',
                                          owner=self)

    @property
    def typeBoogpaal(self):
        """Draagwijdte van de boogpaal."""
        return self._typeBoogpaal.waarde

    @typeBoogpaal.setter
    def typeBoogpaal(self, value):
        self._typeBoogpaal.set_waarde(value, owner=self)
