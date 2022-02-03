# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class LS(EMObject):
    """Laagspanningsaansluiting. Deze zit meestal in een Kast of Cabine (behuizing) en voedt meestal een LSDeel."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#LS'
    label = 'Laagspanningsaansluiting'

    def __init__(self):
        super().__init__()

        self._datumEersteControle = EMAttribuut(field=DateField,
                                                naam='datum eerste controle',
                                                label='datum eerste controle',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.datumEersteControle',
                                                definitie='Definitie nog toe te voegen voor eigenschap datum eerste controle',
                                                owner=self)

        self._datumLaatsteKeuring = EMAttribuut(field=DateField,
                                                naam='datum laatste keuring',
                                                label='datum laatste keuring',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.datumLaatsteKeuring',
                                                definitie='Definitie nog toe te voegen voor eigenschap datum laatste keuring',
                                                owner=self)

        self._datumRisicoanalyse = EMAttribuut(field=DateField,
                                               naam='datum risicoanalyse',
                                               label='datum risicoanalyse',
                                               objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.datumRisicoanalyse',
                                               definitie='Definitie nog toe te voegen voor eigenschap datum risicoanalyse',
                                               owner=self)

        self._installatieverantwConformArt266Arei = EMAttribuut(field=StringField,
                                                                naam='installatieverantw conform art 266 AREI',
                                                                label='installatieverantw conform art 266 AREI',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.installatieverantwConformArt266Arei',
                                                                definitie='Definitie nog toe te voegen voor eigenschap installatieverantw conform art 266 AREI',
                                                                owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

        self._resultaatKeuring = EMAttribuut(field=StringField,
                                             naam='resultaat keuring',
                                             label='resultaat keuring',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.resultaatKeuring',
                                             definitie='Definitie nog toe te voegen voor eigenschap resultaat keuring',
                                             owner=self)

    @property
    def datumEersteControle(self):
        """Definitie nog toe te voegen voor eigenschap datum eerste controle"""
        return self._datumEersteControle.waarde

    @datumEersteControle.setter
    def datumEersteControle(self, value):
        self._datumEersteControle.set_waarde(value, owner=self)

    @property
    def datumLaatsteKeuring(self):
        """Definitie nog toe te voegen voor eigenschap datum laatste keuring"""
        return self._datumLaatsteKeuring.waarde

    @datumLaatsteKeuring.setter
    def datumLaatsteKeuring(self, value):
        self._datumLaatsteKeuring.set_waarde(value, owner=self)

    @property
    def datumRisicoanalyse(self):
        """Definitie nog toe te voegen voor eigenschap datum risicoanalyse"""
        return self._datumRisicoanalyse.waarde

    @datumRisicoanalyse.setter
    def datumRisicoanalyse(self, value):
        self._datumRisicoanalyse.set_waarde(value, owner=self)

    @property
    def installatieverantwConformArt266Arei(self):
        """Definitie nog toe te voegen voor eigenschap installatieverantw conform art 266 AREI"""
        return self._installatieverantwConformArt266Arei.waarde

    @installatieverantwConformArt266Arei.setter
    def installatieverantwConformArt266Arei(self, value):
        self._installatieverantwConformArt266Arei.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

    @property
    def resultaatKeuring(self):
        """Definitie nog toe te voegen voor eigenschap resultaat keuring"""
        return self._resultaatKeuring.waarde

    @resultaatKeuring.setter
    def resultaatKeuring(self, value):
        self._resultaatKeuring.set_waarde(value, owner=self)

