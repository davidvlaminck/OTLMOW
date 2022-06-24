# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KwantWrdInEuro import KwantWrdInEuro
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderdoorboring(AbstracteAanvullendeGeometrie, LijnGeometrie):
    """Gebruikt voor de registratie van kenmerken en de geometrie van een boring onder een weg of spoorweg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AbstracteAanvullendeGeometrie.__init__(self)
        LijnGeometrie.__init__(self)

        self._retributie = OTLAttribuut(field=KwantWrdInEuro,
                                        naam='retributie',
                                        label='retributie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring.retributie',
                                        definition='Periodieke geldsom verschuldigd aan de eigenaar of beheerder van het terrein waaronder de onderboring ligt.',
                                        owner=self)

        self._vergunning = OTLAttribuut(field=DtcDocument,
                                        naam='vergunning',
                                        label='vergunning',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring.vergunning',
                                        definition='Het document met de vergunning voor de onderdoorboring.',
                                        owner=self)

    @property
    def retributie(self):
        """Periodieke geldsom verschuldigd aan de eigenaar of beheerder van het terrein waaronder de onderboring ligt."""
        return self._retributie.get_waarde()

    @retributie.setter
    def retributie(self, value):
        self._retributie.set_waarde(value, owner=self)

    @property
    def vergunning(self):
        """Het document met de vergunning voor de onderdoorboring."""
        return self._vergunning.get_waarde()

    @vergunning.setter
    def vergunning(self, value):
        self._vergunning.set_waarde(value, owner=self)
