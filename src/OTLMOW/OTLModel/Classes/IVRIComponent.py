# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Software import Software
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlIVRIBaseline import KlIVRIBaseline


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVRIComponent(Software):
    """Abstracte die eigenschappen van de iVRI (intelligente verkeersregelaar) component bundelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._baseline = OTLAttribuut(field=KlIVRIBaseline,
                                      naam='baseline',
                                      label='baseline',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.baseline',
                                      definition='Specificatieversie van het protocol waarop de iVRI component werkt.',
                                      owner=self)

        self._certificaat = OTLAttribuut(field=DtcDocument,
                                         naam='certificaat',
                                         label='certificaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.certificaat',
                                         definition='Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. ',
                                         owner=self)

    @property
    def baseline(self):
        """Specificatieversie van het protocol waarop de iVRI component werkt."""
        return self._baseline.waarde

    @baseline.setter
    def baseline(self, value):
        self._baseline.set_waarde(value, owner=self)

    @property
    def certificaat(self):
        """Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. """
        return self._certificaat.waarde

    @certificaat.setter
    def certificaat(self, value):
        self._certificaat.set_waarde(value, owner=self)
