# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Buitenkast import Buitenkast
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlWegkantkastType import KlWegkantkastType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegkantkast(Buitenkast):
    """Behuizing in de vorm van een kast typisch gebruikt buiten, langs de kant van de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord')

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.elektrischSchema',
                                              definition='Elektrisch aansluitschema van de kast.',
                                              owner=self)

        self._heeftMaaibescherming = OTLAttribuut(field=BooleanField,
                                                  naam='heeftMaaibescherming',
                                                  label='heeft maaibescherming',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.heeftMaaibescherming',
                                                  definition='Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast.',
                                                  owner=self)

        self._mplan = OTLAttribuut(field=DtcDocument,
                                   naam='mplan',
                                   label='m-plan',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.mplan',
                                   usagenote='Bestanden van het type dwg of pdf.',
                                   kardinaliteit_max='*',
                                   definition='Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten.',
                                   owner=self)

        self._type = OTLAttribuut(field=KlWegkantkastType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.type',
                                  definition='Type van de wegkantkast volgens de gangbare types.',
                                  owner=self)

    @property
    def elektrischSchema(self):
        """Elektrisch aansluitschema van de kast."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def heeftMaaibescherming(self):
        """Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast."""
        return self._heeftMaaibescherming.get_waarde()

    @heeftMaaibescherming.setter
    def heeftMaaibescherming(self, value):
        self._heeftMaaibescherming.set_waarde(value, owner=self)

    @property
    def mplan(self):
        """Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten."""
        return self._mplan.get_waarde()

    @mplan.setter
    def mplan(self, value):
        self._mplan.set_waarde(value, owner=self)

    @property
    def type(self):
        """Type van de wegkantkast volgens de gangbare types."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
