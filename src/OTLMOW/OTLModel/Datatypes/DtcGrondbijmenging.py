# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlGrondBijmengingHoeveelheidCode import KlGrondBijmengingHoeveelheidCode
from OTLMOW.OTLModel.Datatypes.KlGrondHoofdnaamCode import KlGrondHoofdnaamCode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondbijmengingWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._bijmengingshoofdnaamcode = OTLAttribuut(field=KlGrondHoofdnaamCode,
                                                      naam='bijmengingshoofdnaamcode',
                                                      label='bijmengingshoofdnaamcode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.bijmengingshoofdnaamcode',
                                                      usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                                      definition='Lithologisch nevenbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                                      owner=self)

        self._hoeveelheidscode = OTLAttribuut(field=KlGrondBijmengingHoeveelheidCode,
                                              naam='hoeveelheidscode',
                                              label='hoeveelheidscode',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.hoeveelheidscode',
                                              usagenote=' https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdBijmengingHoeveelheidEnumType)',
                                              definition='Aanduiding (als code) van de hoeveelheid bijmenging.',
                                              owner=self)

        self._isPlaatselijk = OTLAttribuut(field=BooleanField,
                                           naam='isPlaatselijk',
                                           label='is grondmenging plaatselijk',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.isPlaatselijk',
                                           definition='Grondbijmenging plaatselijk of niet-plaatselijk.',
                                           owner=self)

    @property
    def bijmengingshoofdnaamcode(self):
        """Lithologisch nevenbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._bijmengingshoofdnaamcode.waarde

    @bijmengingshoofdnaamcode.setter
    def bijmengingshoofdnaamcode(self, value):
        self._bijmengingshoofdnaamcode.set_waarde(value, owner=self._parent)

    @property
    def hoeveelheidscode(self):
        """Aanduiding (als code) van de hoeveelheid bijmenging."""
        return self._hoeveelheidscode.waarde

    @hoeveelheidscode.setter
    def hoeveelheidscode(self, value):
        self._hoeveelheidscode.set_waarde(value, owner=self._parent)

    @property
    def isPlaatselijk(self):
        """Grondbijmenging plaatselijk of niet-plaatselijk."""
        return self._isPlaatselijk.waarde

    @isPlaatselijk.setter
    def isPlaatselijk(self, value):
        self._isPlaatselijk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondbijmenging(ComplexField, AttributeInfo):
    """Complex datatype om extra informatie van de bijmenging van grond te capteren."""
    naam = 'DtcGrondbijmenging'
    label = 'Grondbijmenging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging'
    definition = 'Complex datatype om extra informatie van de bijmenging van grond te capteren.'
    waardeObject = DtcGrondbijmengingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

