# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.KlPadNetwerkprotectie import KlPadNetwerkprotectie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pad(NaampadObject):
    """Een aaneengesloten reeks van links die samen een verbinding realiseren over het netwerk, gebruik makende van eenzelfde technologie (vb SDH, OTN…)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._netwerkprotectie = OTLAttribuut(field=KlPadNetwerkprotectie,
                                              naam='netwerkprotectie',
                                              label='netwerkprotectie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad.netwerkprotectie',
                                              kardinaliteit_max='*',
                                              definition='Referentie van het pad dat redundantie levert aan dit pad.')

    @property
    def netwerkprotectie(self):
        """Referentie van het pad dat redundantie levert aan dit pad."""
        return self._netwerkprotectie.waarde

    @netwerkprotectie.setter
    def netwerkprotectie(self, value):
        self._netwerkprotectie.set_waarde(value, owner=self)
