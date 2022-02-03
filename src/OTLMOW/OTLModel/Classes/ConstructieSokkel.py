# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLMOW.OTLModel.Classes.BetonnenConstructieElement import BetonnenConstructieElement
from OTLMOW.OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInCm import DtcAfmetingBxlxhInCm
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ConstructieSokkel(ConstructieElement, BetonnenConstructieElement, ConstructieElementenGC, VlakGeometrie):
    """Betonnen zool die het object dat erop rust verhoogt of dat dient om een structuur op een goede manier te kunnen opleggen/verbinden met de fundering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BetonnenConstructieElement.__init__(self)
        ConstructieElement.__init__(self)
        ConstructieElementenGC.__init__(self)
        VlakGeometrie.__init__(self)

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInCm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel.afmetingen',
                                        definition='De afmetingen van de constructiesokkel.',
                                        owner=self)

    @property
    def afmetingen(self):
        """De afmetingen van de constructiesokkel."""
        return self._afmetingen.waarde

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)
