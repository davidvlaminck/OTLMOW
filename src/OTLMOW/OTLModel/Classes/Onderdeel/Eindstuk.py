# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AfschermendeConstructie import AfschermendeConstructie
from OTLMOW.OTLModel.Datatypes.KlLEACTypeEindstuk import KlLEACTypeEindstuk
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Eindstuk(AfschermendeConstructie, LijnGeometrie):
    """Een niet-gecertificeerd einde aan een geleideconstructie, aan de stroomafwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfschermendeConstructie.__init__(self)
        LijnGeometrie.__init__(self)

        self._type = OTLAttribuut(field=KlLEACTypeEindstuk,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk.type',
                                  definition='De vorm van het eindstuk.',
                                  owner=self)

    @property
    def type(self):
        """De vorm van het eindstuk."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
