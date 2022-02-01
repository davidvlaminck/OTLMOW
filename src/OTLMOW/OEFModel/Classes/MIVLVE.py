# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class MIVLVE(EMObject):
    """Meetpunten op snelwegen LVE"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#MIVLVE'
    label = 'MIVLVE'

    def __init__(self):
        super().__init__()

        self._bezoeklocatieLatitude5052 = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='Bezoeklocatie Latitude (50-52)',
                                                      label='Bezoeklocatie Latitude (50-52)',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.bezoeklocatieLatitude5052',
                                                      definitie='waardes tussen 50 en 52')

        self._bezoeklocatieLongitude27 = EMAttribuut(field=FloatOrDecimalField,
                                                     naam='Bezoeklocatie Longitude (2-7)',
                                                     label='Bezoeklocatie Longitude (2-7)',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.bezoeklocatieLongitude27',
                                                     definitie='waardes tussen 2 en 7')

        self._opmerkingen = EMAttribuut(field=StringField,
                                        naam='Opmerkingen',
                                        label='Opmerkingen',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingen',
                                        definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen')

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie')

    @property
    def bezoeklocatieLatitude5052(self):
        """waardes tussen 50 en 52"""
        return self._bezoeklocatieLatitude5052.waarde

    @bezoeklocatieLatitude5052.setter
    def bezoeklocatieLatitude5052(self, value):
        self._bezoeklocatieLatitude5052.set_waarde(value, owner=self)

    @property
    def bezoeklocatieLongitude27(self):
        """waardes tussen 2 en 7"""
        return self._bezoeklocatieLongitude27.waarde

    @bezoeklocatieLongitude27.setter
    def bezoeklocatieLongitude27(self, value):
        self._bezoeklocatieLongitude27.set_waarde(value, owner=self)

    @property
    def opmerkingen(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen"""
        return self._opmerkingen.waarde

    @opmerkingen.setter
    def opmerkingen(self, value):
        self._opmerkingen.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

