# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class RSSBord(EMObject):
    """Dynamische borden : variabel rijstrooksignalisatiebord (def. SB 270 hfdst 50)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RSSBord'
    label = 'RSS bord'

    def __init__(self):
        super().__init__()

        self._rssBuitenGebruik = EMAttribuut(field=BooleanField,
                                             naam='RSS buiten gebruik',
                                             label='RSS buiten gebruik',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RSSBord.rssBuitenGebruik',
                                             definitie='Definitie nog toe te voegen voor eigenschap RSS buiten gebruik')

        self._datumNieuweRss = EMAttribuut(field=DateField,
                                           naam='datum nieuwe RSS',
                                           label='datum nieuwe RSS',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RSSBord.datumNieuweRss',
                                           definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe RSS')

        self._drager = EMAttribuut(field=StringField,
                                   naam='drager',
                                   label='drager',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.drager',
                                   definitie='Definitie nog toe te voegen voor eigenschap drager')

        self._redenRssBuitenGebruik = EMAttribuut(field=StringField,
                                                  naam='reden RSS buiten gebruik',
                                                  label='reden RSS buiten gebruik',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RSSBord.redenRssBuitenGebruik',
                                                  definitie='Definitie nog toe te voegen voor eigenschap reden RSS buiten gebruik')

    @property
    def rssBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap RSS buiten gebruik"""
        return self._rssBuitenGebruik.waarde

    @rssBuitenGebruik.setter
    def rssBuitenGebruik(self, value):
        self._rssBuitenGebruik.set_waarde(value, owner=self)

    @property
    def datumNieuweRss(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe RSS"""
        return self._datumNieuweRss.waarde

    @datumNieuweRss.setter
    def datumNieuweRss(self, value):
        self._datumNieuweRss.set_waarde(value, owner=self)

    @property
    def drager(self):
        """Definitie nog toe te voegen voor eigenschap drager"""
        return self._drager.waarde

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)

    @property
    def redenRssBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden RSS buiten gebruik"""
        return self._redenRssBuitenGebruik.waarde

    @redenRssBuitenGebruik.setter
    def redenRssBuitenGebruik(self, value):
        self._redenRssBuitenGebruik.set_waarde(value, owner=self)

