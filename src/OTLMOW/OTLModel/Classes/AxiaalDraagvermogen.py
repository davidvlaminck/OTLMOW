# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton


# Generated with OTLClassCreator. To modify: extend, do not edit
class AxiaalDraagvermogen(ABC):
    """Abstracte voor de bundeling van de axiale druk- en trekdraagvermogens, berekend volgens verschillende grenstoestanden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._drukdraagvermogenGGT = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                  naam='drukdraagvermogenGGT',
                                                  label='drukdraagvermogen in gebruiksgrenstoestanden',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogen.drukdraagvermogenGGT',
                                                  definition='Karakteristieke waarde van de maximale druklast die een constructie-element kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton.',
                                                  owner=self)

        self._drukdraagvermogenUGT = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                  naam='drukdraagvermogenUGT',
                                                  label='drukdraagvermogen in uiterste grenstoestand',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogen.drukdraagvermogenUGT',
                                                  definition='Drukdraagvermogen, uitgedrukt in kilonewton, in uiterste grenstoestand (UGT) design approach DA1/1.',
                                                  owner=self)

        self._trekdraagvermorgenGGT = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                   naam='trekdraagvermorgenGGT',
                                                   label='trekdraagvermogen in gebruiksgrenstoestanden',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogen.trekdraagvermorgenGGT',
                                                   definition='Karakteristieke waarde van de maximale treklast die een constructie-element kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton.',
                                                   owner=self)

        self._trekdraagvermorgenUGT = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                   naam='trekdraagvermorgenUGT',
                                                   label='trekdraagvermogen in uiterste grenstoestand',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogen.trekdraagvermorgenUGT',
                                                   definition='Trekdraagvermogen, uitgedrukt in kilonewton, in uiterste grenstoestand (UGT) design approach DA1/1.',
                                                   owner=self)

    @property
    def drukdraagvermogenGGT(self):
        """Karakteristieke waarde van de maximale druklast die een constructie-element kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton."""
        return self._drukdraagvermogenGGT.get_waarde()

    @drukdraagvermogenGGT.setter
    def drukdraagvermogenGGT(self, value):
        self._drukdraagvermogenGGT.set_waarde(value, owner=self)

    @property
    def drukdraagvermogenUGT(self):
        """Drukdraagvermogen, uitgedrukt in kilonewton, in uiterste grenstoestand (UGT) design approach DA1/1."""
        return self._drukdraagvermogenUGT.get_waarde()

    @drukdraagvermogenUGT.setter
    def drukdraagvermogenUGT(self, value):
        self._drukdraagvermogenUGT.set_waarde(value, owner=self)

    @property
    def trekdraagvermorgenGGT(self):
        """Karakteristieke waarde van de maximale treklast die een constructie-element kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton."""
        return self._trekdraagvermorgenGGT.get_waarde()

    @trekdraagvermorgenGGT.setter
    def trekdraagvermorgenGGT(self, value):
        self._trekdraagvermorgenGGT.set_waarde(value, owner=self)

    @property
    def trekdraagvermorgenUGT(self):
        """Trekdraagvermogen, uitgedrukt in kilonewton, in uiterste grenstoestand (UGT) design approach DA1/1."""
        return self._trekdraagvermorgenUGT.get_waarde()

    @trekdraagvermorgenUGT.setter
    def trekdraagvermorgenUGT(self, value):
        self._trekdraagvermorgenUGT.set_waarde(value, owner=self)
