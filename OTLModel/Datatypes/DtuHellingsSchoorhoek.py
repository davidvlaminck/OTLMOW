# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.KlSchoorhoek import KlSchoorhoek
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuHellingsSchoorhoekAttributen(AttributeInfo):
    def __init__(self):
        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.hellingshoek',
                                          definition='Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden.')

        self._schoorhoek = OTLAttribuut(field=KlSchoorhoek,
                                        naam='schoorhoek',
                                        label='schoorhoek',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.schoorhoek',
                                        definition='Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4).')

    @property
    def hellingshoek(self):
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden."""
        return self._hellingshoek.waarde

    @property
    def schoorhoek(self):
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4)."""
        return self._schoorhoek.waarde


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuHellingsSchoorhoek(UnionTypeField, AttributeInfo):
    """Union datatype voor de hellings- of de schoorhoek."""
    naam = 'DtuHellingsSchoorhoek'
    label = 'Hellings- of schoorhoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek'
    definition = 'Union datatype voor de hellings- of de schoorhoek.'
    waardeObject = DtuHellingsSchoorhoekAttributen

    def __str__(self):
        return UnionTypeField.__str__(self)

