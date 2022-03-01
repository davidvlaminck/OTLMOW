# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProductidentificatiecodeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._keuringsverslag = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsverslag',
                                             label='keuringsverslag',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.keuringsverslag',
                                             definition='Een rapport met de resultaten van de keuring.',
                                             owner=self)

        self._linkTechnischeFiche = OTLAttribuut(field=URIField,
                                                 naam='linkTechnischeFiche',
                                                 label='link technische fiche',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.linkTechnischeFiche',
                                                 definition='De link naar de technische fiche van het gerelateerd product.',
                                                 owner=self)

        self._producent = OTLAttribuut(field=StringField,
                                       naam='producent',
                                       label='producent',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.producent',
                                       definition='De gerelateerde fabrikant.',
                                       owner=self)

        self._productidentificatiecode = OTLAttribuut(field=StringField,
                                                      naam='productidentificatiecode',
                                                      label='productidentificatiecode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.productidentificatiecode',
                                                      definition='De code van het gebruikte product (COPRO/BENOR).',
                                                      owner=self)

    @property
    def keuringsverslag(self):
        """Een rapport met de resultaten van de keuring."""
        return self._keuringsverslag.waarde

    @keuringsverslag.setter
    def keuringsverslag(self, value):
        self._keuringsverslag.set_waarde(value, owner=self._parent)

    @property
    def linkTechnischeFiche(self):
        """De link naar de technische fiche van het gerelateerd product."""
        return self._linkTechnischeFiche.waarde

    @linkTechnischeFiche.setter
    def linkTechnischeFiche(self, value):
        self._linkTechnischeFiche.set_waarde(value, owner=self._parent)

    @property
    def producent(self):
        """De gerelateerde fabrikant."""
        return self._producent.waarde

    @producent.setter
    def producent(self, value):
        self._producent.set_waarde(value, owner=self._parent)

    @property
    def productidentificatiecode(self):
        """De code van het gebruikte product (COPRO/BENOR)."""
        return self._productidentificatiecode.waarde

    @productidentificatiecode.setter
    def productidentificatiecode(self, value):
        self._productidentificatiecode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProductidentificatiecode(ComplexField, AttributeInfo):
    """Complex datatype dat alle nodige informatie van het product capteert."""
    naam = 'DtcProductidentificatiecode'
    label = 'Productidentificatiecode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode'
    definition = 'Complex datatype dat alle nodige informatie van het product capteert.'
    waardeObject = DtcProductidentificatiecodeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

