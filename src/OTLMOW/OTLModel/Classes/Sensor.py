# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sensor(ABC):
    """Abstracte om de eigenschappen en relaties van alle sensoren te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._kalibratiecertificaat = OTLAttribuut(field=DtcDocument,
                                                   naam='kalibratiecertificaat',
                                                   label='kalibratiecertificaat',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor.kalibratiecertificaat',
                                                   definition='Een kwaliteitsdocument dat aangeeft of de testresultaten van de sensor al dan niet binnen de vereiste bedrijfsspecificaties vallen.',
                                                   owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technsiche fiche als bijlage van de sensor.',
                                             owner=self)

    @property
    def kalibratiecertificaat(self):
        """Een kwaliteitsdocument dat aangeeft of de testresultaten van de sensor al dan niet binnen de vereiste bedrijfsspecificaties vallen."""
        return self._kalibratiecertificaat.get_waarde()

    @kalibratiecertificaat.setter
    def kalibratiecertificaat(self, value):
        self._kalibratiecertificaat.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technsiche fiche als bijlage van de sensor."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
