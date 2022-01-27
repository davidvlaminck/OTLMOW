# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.SelNietSelLus import SelNietSelLus
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlSelLusSoort import KlSelLusSoort
from OTLMOW.OTLModel.Datatypes.KlSelLusVerbinding import KlSelLusVerbinding


# Generated with OTLClassCreator. To modify: extend, do not edit
class SelectieveDetectielus(SelNietSelLus):
    """De selectieve detectielussen moeten bepaalde voertuigen toelaten het kruispunt prioritair te dwarsen. Daarvoor zijn die prioritaire voertuigen uitgerust met een zendtoestel dat gecodeerd informatie doorstuurt naar een datalus in het wegdek. Deze lus is verbonden met een demodulator die de informatie decodeert en doorstuurt naar de verkeersregelaar van het te dwarsen kruispunt"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftMeerdereKruisingen = OTLAttribuut(field=BooleanField,
                                                     naam='heeftMeerdereKruisingen',
                                                     label='heeft meerdere kruisingen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.heeftMeerdereKruisingen',
                                                     definition='Aanduiding of de lus voor meerdere kruispunten wordt gebruikt.')

        self._soortLus = OTLAttribuut(field=KlSelLusSoort,
                                      naam='soortLus',
                                      label='soort lus',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.soortLus',
                                      kardinaliteit_max='*',
                                      definition='Type detectielus vb bus, tram,...')

        self._verbinding = OTLAttribuut(field=KlSelLusVerbinding,
                                        naam='verbinding',
                                        label='verbinding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.verbinding',
                                        definition='Soort verbinding (serieel of contact).')

    @property
    def heeftMeerdereKruisingen(self):
        """Aanduiding of de lus voor meerdere kruispunten wordt gebruikt."""
        return self._heeftMeerdereKruisingen.waarde

    @heeftMeerdereKruisingen.setter
    def heeftMeerdereKruisingen(self, value):
        self._heeftMeerdereKruisingen.set_waarde(value, owner=self)

    @property
    def soortLus(self):
        """Type detectielus vb bus, tram,..."""
        return self._soortLus.waarde

    @soortLus.setter
    def soortLus(self, value):
        self._soortLus.set_waarde(value, owner=self)

    @property
    def verbinding(self):
        """Soort verbinding (serieel of contact)."""
        return self._verbinding.waarde

    @verbinding.setter
    def verbinding(self, value):
        self._verbinding.set_waarde(value, owner=self)
