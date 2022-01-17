# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KlConstructiestaalsoort import KlConstructiestaalsoort
from OTLModel.Datatypes.KlWalsmethode import KlWalsmethode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcConstructiestaalspecificatiesWaarden(AttributeInfo):
    def __init__(self):
        self._staalsoort = OTLAttribuut(field=KlConstructiestaalsoort,
                                        naam='staalsoort',
                                        label='staalsoort',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.staalsoort',
                                        definition='Staalkwaliteit die wordt gebruikt volgens Europese normen.')

        self._walsmethode = OTLAttribuut(field=KlWalsmethode,
                                         naam='walsmethode',
                                         label='walsmethode',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.walsmethode',
                                         definition='Op welke manier het staal gewalst is.')

    @property
    def staalsoort(self):
        """Staalkwaliteit die wordt gebruikt volgens Europese normen."""
        return self._staalsoort.waarde

    @staalsoort.setter
    def staalsoort(self, value):
        self._staalsoort.set_waarde(value)

    @property
    def walsmethode(self):
        """Op welke manier het staal gewalst is."""
        return self._walsmethode.waarde

    @walsmethode.setter
    def walsmethode(self, value):
        self._walsmethode.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcConstructiestaalspecificaties(ComplexField, AttributeInfo):
    """Complex datatype om de eigenschappen van constructiestaal te bundelen."""
    naam = 'DtcConstructiestaalspecificaties'
    label = 'Constructiestaalspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties'
    definition = 'Complex datatype om de eigenschappen van constructiestaal te bundelen.'
    waardeObject = DtcConstructiestaalspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

