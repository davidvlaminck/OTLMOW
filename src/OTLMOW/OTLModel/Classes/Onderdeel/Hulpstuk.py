# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.LinkendElement import LinkendElement
from OTLMOW.OTLModel.Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from OTLMOW.OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from OTLMOW.OTLModel.Datatypes.KlHulpstukType import KlHulpstukType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulpstuk(LinkendElement, OmhullendeInrichting, PuntGeometrie):
    """Stukken die zorgen voor verbindingen tussen rechte buizen om bv. van richting te veranderen, te verlengen, te verlopen van diameter, meerdere buizen op mekaar aan te sluiten,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        LinkendElement.__init__(self)
        OmhullendeInrichting.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis')

        self._inwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='inwendigeDiameter',
                                               label='inwendige diameter',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.inwendigeDiameter',
                                               definition='De diameter van de binnenzijde van het hulpstuk in millimeter.',
                                               owner=self)

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.materiaal',
                                       definition='Het materiaal waaruit het hulpstuk vervaardigd is.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlHulpstukType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.type',
                                  definition='Het type van het hulpstuk.',
                                  owner=self)

        self._uitwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='uitwendigeDiameter',
                                                label='uitwendige diameter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.uitwendigeDiameter',
                                                definition='De diameter van de buitenzijde van het hulpstuk in millimeter.',
                                                owner=self)

    @property
    def inwendigeDiameter(self):
        """De diameter van de binnenzijde van het hulpstuk in millimeter."""
        return self._inwendigeDiameter.get_waarde()

    @inwendigeDiameter.setter
    def inwendigeDiameter(self, value):
        self._inwendigeDiameter.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit het hulpstuk vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van het hulpstuk."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def uitwendigeDiameter(self):
        """De diameter van de buitenzijde van het hulpstuk in millimeter."""
        return self._uitwendigeDiameter.get_waarde()

    @uitwendigeDiameter.setter
    def uitwendigeDiameter(self, value):
        self._uitwendigeDiameter.set_waarde(value, owner=self)
