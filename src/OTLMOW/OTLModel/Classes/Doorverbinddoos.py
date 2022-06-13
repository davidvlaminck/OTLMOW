# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Behuizing import Behuizing
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLMOW.OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Doorverbinddoos(Behuizing, PuntGeometrie):
    """Een behuizing waarin kabels aan elkaar gekoppeld worden om over te gaan van het ene naar het andere type of de splitsen of samen te komen. De behuizing is niet voorzien van een deur en kan enkel geopend worden met het geschikte gereedschap."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Behuizing.__init__(self)
        PuntGeometrie.__init__(self)

        self._buitenafmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                              naam='buitenafmetingen',
                                              label='buitenafmetingen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos.buitenafmetingen',
                                              definition='De afmeting van de buitenkant van de doorverbinddoos.',
                                              owner=self)

        self._ipKlasse = OTLAttribuut(field=KlAlgIngressProtectionCode,
                                      naam='ipKlasse',
                                      label='ingress protection klasse',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos.ipKlasse',
                                      definition='De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.',
                                      owner=self)

    @property
    def buitenafmetingen(self):
        """De afmeting van de buitenkant van de doorverbinddoos."""
        return self._buitenafmetingen.get_waarde()

    @buitenafmetingen.setter
    def buitenafmetingen(self, value):
        self._buitenafmetingen.set_waarde(value, owner=self)

    @property
    def ipKlasse(self):
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
        return self._ipKlasse.get_waarde()

    @ipKlasse.setter
    def ipKlasse(self, value):
        self._ipKlasse.set_waarde(value, owner=self)
