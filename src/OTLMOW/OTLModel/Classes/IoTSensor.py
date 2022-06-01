# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcCompacteBatterij import DtcCompacteBatterij
from OTLMOW.OTLModel.Datatypes.KlIoTSensorMerk import KlIoTSensorMerk
from OTLMOW.OTLModel.Datatypes.KlIoTSensorModelnaam import KlIoTSensorModelnaam
from OTLMOW.OTLModel.Datatypes.KlIoTSensorParameter import KlIoTSensorParameter
from OTLMOW.OTLModel.Datatypes.KlIoTSensorVerbindingstype import KlIoTSensorVerbindingstype


# Generated with OTLClassCreator. To modify: extend, do not edit
class IoTSensor(AIMNaamObject):
    """Een sensor die veranderingen in de omgeving registreert en erop reageert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._batterij = OTLAttribuut(field=DtcCompacteBatterij,
                                      naam='batterij',
                                      label='batterij',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.batterij',
                                      definition='Bevat de informatie van de inwendige compacte batterij.',
                                      owner=self)

        self._gemetenParameters = OTLAttribuut(field=KlIoTSensorParameter,
                                               naam='gemetenParameters',
                                               label='gemeten parameters',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.gemetenParameters',
                                               kardinaliteit_max='*',
                                               definition='De mogelijke parameters die kunnen gemeten worden door de IoT-sensor.',
                                               owner=self)

        self._merk = OTLAttribuut(field=KlIoTSensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.merk',
                                  definition='Het merk van een IoT-sensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIoTSensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.modelnaam',
                                       definition='De modelnaam van een IoT-sensor.',
                                       owner=self)

        self._typeVerbinding = OTLAttribuut(field=KlIoTSensorVerbindingstype,
                                            naam='typeVerbinding',
                                            label='type verbinding',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.typeVerbinding',
                                            definition='De manier van de communicatieverbinding van de IoT-sensor.',
                                            owner=self)

    @property
    def batterij(self):
        """Bevat de informatie van de inwendige compacte batterij."""
        return self._batterij.get_waarde()

    @batterij.setter
    def batterij(self, value):
        self._batterij.set_waarde(value, owner=self)

    @property
    def gemetenParameters(self):
        """De mogelijke parameters die kunnen gemeten worden door de IoT-sensor."""
        return self._gemetenParameters.get_waarde()

    @gemetenParameters.setter
    def gemetenParameters(self, value):
        self._gemetenParameters.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van een IoT-sensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van een IoT-sensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def typeVerbinding(self):
        """De manier van de communicatieverbinding van de IoT-sensor."""
        return self._typeVerbinding.get_waarde()

    @typeVerbinding.setter
    def typeVerbinding(self, value):
        self._typeVerbinding.set_waarde(value, owner=self)
