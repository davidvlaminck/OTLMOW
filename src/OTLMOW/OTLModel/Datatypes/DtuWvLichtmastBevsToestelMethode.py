# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastBevsToestel import KlWvLichtmastBevsToestel
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuWvLichtmastBevsToestelMethodeWaarden(AttributeInfo, UnionWaarden):
    def __init__(self):
        super().__init__()
        self._afwijkendeMethode = OTLAttribuut(field=StringField,
                                               naam='afwijkendeMethode',
                                               label='afwijkende methode',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode.afwijkendeMethode',
                                               kardinaliteit_min='0',
                                               definition='Tekstveld waarin de afwijkende methode van bevestiging van verlichtingstoestel aan lichtmast kan beschreven worden.',
                                               owner=self)

        self._standaardMethode = OTLAttribuut(field=KlWvLichtmastBevsToestel,
                                              naam='standaardMethode',
                                              label='standaard methode',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode.standaardMethode',
                                              kardinaliteit_min='0',
                                              definition='Bepaling van de standaardbevestigingen van verlichtingstoestellen aan lichtmasten.',
                                              owner=self)

    @property
    def afwijkendeMethode(self):
        """Tekstveld waarin de afwijkende methode van bevestiging van verlichtingstoestel aan lichtmast kan beschreven worden."""
        return self._afwijkendeMethode.waarde

    @afwijkendeMethode.setter
    def afwijkendeMethode(self, value):
        self._afwijkendeMethode.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_afwijkendeMethode')

    @property
    def standaardMethode(self):
        """Bepaling van de standaardbevestigingen van verlichtingstoestellen aan lichtmasten."""
        return self._standaardMethode.waarde

    @standaardMethode.setter
    def standaardMethode(self, value):
        self._standaardMethode.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_standaardMethode')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuWvLichtmastBevsToestelMethode(UnionTypeField, AttributeInfo):
    """Union datatype voor de wijze waarop verlichtingstoestellen bevestigd zijn op een lichtmast, indien dit een standaard methode is dan kan deze geselecteerd worden uit een keuzelijst. Bij afwijkende methode kan de methode toegelicht worden."""
    naam = 'DtuWvLichtmastBevsToestelMethode'
    label = 'Bevestiging wegverlichtingstoestel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode'
    definition = 'Union datatype voor de wijze waarop verlichtingstoestellen bevestigd zijn op een lichtmast, indien dit een standaard methode is dan kan deze geselecteerd worden uit een keuzelijst. Bij afwijkende methode kan de methode toegelicht worden.'
    waardeObject = DtuWvLichtmastBevsToestelMethodeWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

