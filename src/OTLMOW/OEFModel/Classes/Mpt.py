# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Mpt(EMObject):
    """Meetpunt op snelwegen"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Mpt'
    label = 'MIV meetpunt'

    def __init__(self):
        super().__init__()

        self._aansluiting = EMAttribuut(field=StringField,
                                        naam='Aansluiting',
                                        label='Aansluiting',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.aansluiting',
                                        definitie='Definitie nog toe te voegen voor eigenschap Aansluiting')

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

        self._details = EMAttribuut(field=StringField,
                                    naam='Details',
                                    label='Details',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.details',
                                    definitie='Details van het formaat')

        self._formaat = EMAttribuut(field=StringField,
                                    naam='Formaat',
                                    label='Formaat',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.formaat',
                                    definitie='Definitie nog toe te voegen voor eigenschap Formaat')

        self._gekoppeld = EMAttribuut(field=BooleanField,
                                      naam='Gekoppeld',
                                      label='Gekoppeld',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.gekoppeld',
                                      definitie='Definitie nog toe te voegen voor eigenschap Gekoppeld')

        self._laag = EMAttribuut(field=StringField,
                                 naam='Laag',
                                 label='Laag',
                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.laag',
                                 definitie='Definitie nog toe te voegen voor eigenschap Laag')

        self._meetpost = EMAttribuut(field=FloatOrDecimalField,
                                     naam='Meetpost',
                                     label='Meetpost',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.meetpost',
                                     definitie='Meetpost van het Verkeerscentrum')

        self._opmerkingen = EMAttribuut(field=StringField,
                                        naam='Opmerkingen',
                                        label='Opmerkingen',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingen',
                                        definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen')

        self._rijstrook = EMAttribuut(field=StringField,
                                      naam='Rijstrook',
                                      label='Rijstrook',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.rijstrook',
                                      definitie='0 = Pechstrook / BOB 1 = Rechtse rijstrook 2-8 = Volgende rijstroken 9 = Spookstrook')

        self._trekput = EMAttribuut(field=BooleanField,
                                    naam='Trekput',
                                    label='Trekput',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.trekput',
                                    definitie='Aanwezigheid van een trekput')

        self._uitslijprichting = EMAttribuut(field=StringField,
                                             naam='Uitslijprichting',
                                             label='Uitslijprichting',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.uitslijprichting',
                                             definitie='Definitie nog toe te voegen voor eigenschap Uitslijprichting')

        self._wegdek = EMAttribuut(field=StringField,
                                   naam='Wegdek',
                                   label='Wegdek',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Mpt.wegdek',
                                   definitie='Definitie nog toe te voegen voor eigenschap Wegdek')

    @property
    def aansluiting(self):
        """Definitie nog toe te voegen voor eigenschap Aansluiting"""
        return self._aansluiting.waarde

    @aansluiting.setter
    def aansluiting(self, value):
        self._aansluiting.set_waarde(value, owner=self)

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
    def details(self):
        """Details van het formaat"""
        return self._details.waarde

    @details.setter
    def details(self, value):
        self._details.set_waarde(value, owner=self)

    @property
    def formaat(self):
        """Definitie nog toe te voegen voor eigenschap Formaat"""
        return self._formaat.waarde

    @formaat.setter
    def formaat(self, value):
        self._formaat.set_waarde(value, owner=self)

    @property
    def gekoppeld(self):
        """Definitie nog toe te voegen voor eigenschap Gekoppeld"""
        return self._gekoppeld.waarde

    @gekoppeld.setter
    def gekoppeld(self, value):
        self._gekoppeld.set_waarde(value, owner=self)

    @property
    def laag(self):
        """Definitie nog toe te voegen voor eigenschap Laag"""
        return self._laag.waarde

    @laag.setter
    def laag(self, value):
        self._laag.set_waarde(value, owner=self)

    @property
    def meetpost(self):
        """Meetpost van het Verkeerscentrum"""
        return self._meetpost.waarde

    @meetpost.setter
    def meetpost(self, value):
        self._meetpost.set_waarde(value, owner=self)

    @property
    def opmerkingen(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen"""
        return self._opmerkingen.waarde

    @opmerkingen.setter
    def opmerkingen(self, value):
        self._opmerkingen.set_waarde(value, owner=self)

    @property
    def rijstrook(self):
        """0 = Pechstrook / BOB 1 = Rechtse rijstrook 2-8 = Volgende rijstroken 9 = Spookstrook"""
        return self._rijstrook.waarde

    @rijstrook.setter
    def rijstrook(self, value):
        self._rijstrook.set_waarde(value, owner=self)

    @property
    def trekput(self):
        """Aanwezigheid van een trekput"""
        return self._trekput.waarde

    @trekput.setter
    def trekput(self, value):
        self._trekput.set_waarde(value, owner=self)

    @property
    def uitslijprichting(self):
        """Definitie nog toe te voegen voor eigenschap Uitslijprichting"""
        return self._uitslijprichting.waarde

    @uitslijprichting.setter
    def uitslijprichting(self, value):
        self._uitslijprichting.set_waarde(value, owner=self)

    @property
    def wegdek(self):
        """Definitie nog toe te voegen voor eigenschap Wegdek"""
        return self._wegdek.waarde

    @wegdek.setter
    def wegdek(self, value):
        self._wegdek.set_waarde(value, owner=self)

