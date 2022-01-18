# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlWegkantkastType import KlWegkantkastType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegkantkast(Buitenkast, AttributeInfo):
    """Behuizing in de vorm van een kast typisch gebruikt buiten, langs de kant van de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Buitenkast.__init__(self)

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.elektrischSchema',
                                              definition='Elektrisch aansluitschema van de kast.')

        self._heeftMaaibescherming = OTLAttribuut(field=BooleanField,
                                                  naam='heeftMaaibescherming',
                                                  label='heeft maaibescherming',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.heeftMaaibescherming',
                                                  definition='Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast.')

        self._mplan = OTLAttribuut(field=DtcDocument,
                                   naam='mplan',
                                   label='m-plan',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.mplan',
                                   usagenote='Bestanden van het type dwg of pdf.',
                                   kardinaliteit_max='*',
                                   definition='Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten.')

        self._type = OTLAttribuut(field=KlWegkantkastType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.type',
                                  definition='Type van de wegkantkast volgens de gangbare types.')

    @property
    def elektrischSchema(self):
        """Elektrisch aansluitschema van de kast."""
        return self._elektrischSchema.waarde

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def heeftMaaibescherming(self):
        """Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast."""
        return self._heeftMaaibescherming.waarde

    @heeftMaaibescherming.setter
    def heeftMaaibescherming(self, value):
        self._heeftMaaibescherming.set_waarde(value, owner=self)

    @property
    def mplan(self):
        """Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten."""
        return self._mplan.waarde

    @mplan.setter
    def mplan(self, value):
        self._mplan.set_waarde(value, owner=self)

    @property
    def type(self):
        """Type van de wegkantkast volgens de gangbare types."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
