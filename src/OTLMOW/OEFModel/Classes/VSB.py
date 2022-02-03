# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class VSB(EMObject):
    """Dynamische borden : Soort van restgroep van allerlei dynamische borden die niet onder een meer specifiek type vallen. Exacte verschil met VGL is me niet duidelijk"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VSB'
    label = 'Veranderlijke signalisatie borden'

    def __init__(self):
        super().__init__()

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

