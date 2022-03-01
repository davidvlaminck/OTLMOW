# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlPoortconfiguratieRichting import KlPoortconfiguratieRichting
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSoftwarePoortconfiguratieWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._poortnummer = OTLAttribuut(field=IntegerField,
                                         naam='poortnummer',
                                         label='poortnummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.poortnummer',
                                         definition='Het nummer dat werd toegekend aan de (netwerk)poort.',
                                         owner=self)

        self._richting = OTLAttribuut(field=KlPoortconfiguratieRichting,
                                      naam='richting',
                                      label='richting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.richting',
                                      definition='De richting waarin de poort openstaat.',
                                      owner=self)

        self._service = OTLAttribuut(field=StringField,
                                     naam='service',
                                     label='service',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.service',
                                     definition='De service die op een bepaalde poort is aangesloten.',
                                     owner=self)

    @property
    def poortnummer(self):
        """Het nummer dat werd toegekend aan de (netwerk)poort."""
        return self._poortnummer.waarde

    @poortnummer.setter
    def poortnummer(self, value):
        self._poortnummer.set_waarde(value, owner=self._parent)

    @property
    def richting(self):
        """De richting waarin de poort openstaat."""
        return self._richting.waarde

    @richting.setter
    def richting(self, value):
        self._richting.set_waarde(value, owner=self._parent)

    @property
    def service(self):
        """De service die op een bepaalde poort is aangesloten."""
        return self._service.waarde

    @service.setter
    def service(self, value):
        self._service.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSoftwarePoortconfiguratie(ComplexField, AttributeInfo):
    """Complex datatype dat beschrijft welke poort voor welke service gebruikt wordt."""
    naam = 'DtcSoftwarePoortconfiguratie'
    label = 'Software poortconfiguratie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie'
    definition = 'Complex datatype dat beschrijft welke poort voor welke service gebruikt wordt.'
    waardeObject = DtcSoftwarePoortconfiguratieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

