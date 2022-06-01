# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcGrondbijmenging import DtcGrondbijmenging
from OTLMOW.OTLModel.Datatypes.KlGrondHoofdnaamCode import KlGrondHoofdnaamCode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondsoortWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._bijmenging = OTLAttribuut(field=DtcGrondbijmenging,
                                        naam='bijmenging',
                                        label='bijmenging',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort.bijmenging',
                                        usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                        kardinaliteit_max='3',
                                        definition='Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                        owner=self)

        self._hoofdnaamcode = OTLAttribuut(field=KlGrondHoofdnaamCode,
                                           naam='hoofdnaamcode',
                                           label='hoofdnaamcode',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort.hoofdnaamcode',
                                           usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                           definition='Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                           owner=self)

    @property
    def bijmenging(self):
        """Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._bijmenging.get_waarde()

    @bijmenging.setter
    def bijmenging(self, value):
        self._bijmenging.set_waarde(value, owner=self._parent)

    @property
    def hoofdnaamcode(self):
        """Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._hoofdnaamcode.get_waarde()

    @hoofdnaamcode.setter
    def hoofdnaamcode(self, value):
        self._hoofdnaamcode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondsoort(ComplexField, AttributeInfo):
    """Complex datatype om het soort grond te bepalen."""
    naam = 'DtcGrondsoort'
    label = 'Grondsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort'
    definition = 'Complex datatype om het soort grond te bepalen.'
    waardeObject = DtcGrondsoortWaarden

    def __str__(self):
        return ComplexField.__str__(self)

