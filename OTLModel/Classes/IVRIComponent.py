# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Software import Software
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlIVRIBaseline import KlIVRIBaseline


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVRIComponent(Software, AttributeInfo):
    """Abstracte die eigenschappen van de iVRI (intelligente verkeersregelaar) component bundelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        Software.__init__(self)

        self._baseline = OTLAttribuut(field=KlIVRIBaseline,
                                      naam='baseline',
                                      label='baseline',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.baseline',
                                      definition='Specificatieversie van het protocol waarop de iVRI component werkt.')

        self._certificaat = OTLAttribuut(field=DtcDocument,
                                         naam='certificaat',
                                         label='certificaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.certificaat',
                                         definition='Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. ')

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
