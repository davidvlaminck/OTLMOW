# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class CCTV(EMObject):
    """GESLOTEN TV-CIRCUIT"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#CCTV'
    label = 'CCTV camera'

    def __init__(self):
        super().__init__()

        self._wifiAntenneAanwezig = EMAttribuut(field=BooleanField,
                                                naam='WIFI antenne aanwezig',
                                                label='WIFI antenne aanwezig',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.wifiAntenneAanwezig',
                                                definitie='Definitie nog toe te voegen voor eigenschap WIFI antenne aanwezig')

        self._datumNieuwVertrekGeplaatst = EMAttribuut(field=DateField,
                                                       naam='datum nieuw vertrek geplaatst',
                                                       label='datum nieuw vertrek geplaatst',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuwVertrekGeplaatst',
                                                       definitie='Definitie nog toe te voegen voor eigenschap datum nieuw vertrek geplaatst')

        self._datumNieuweCamera = EMAttribuut(field=DateField,
                                              naam='datum nieuwe camera',
                                              label='datum nieuwe camera',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweCamera',
                                              definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe camera')

        self._datumNieuweEncoder = EMAttribuut(field=DateField,
                                               naam='datum nieuwe encoder',
                                               label='datum nieuwe encoder',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweEncoder',
                                               definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe encoder')

        self._datumNieuweMediaomvormer = EMAttribuut(field=DateField,
                                                     naam='datum nieuwe mediaomvormer',
                                                     label='datum nieuwe mediaomvormer',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweMediaomvormer',
                                                     definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe mediaomvormer')

        self._encoderAanwezig = EMAttribuut(field=BooleanField,
                                            naam='encoder aanwezig?',
                                            label='encoder aanwezig?',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig',
                                            definitie='Definitie nog toe te voegen voor eigenschap encoder aanwezig?')

        self._encoderInExterneKast = EMAttribuut(field=BooleanField,
                                                 naam='encoder in externe kast',
                                                 label='encoder in externe kast',
                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderInExterneKast',
                                                 definitie='Definitie nog toe te voegen voor eigenschap encoder in externe kast')

        self._mediaomvormerAanwezig = EMAttribuut(field=BooleanField,
                                                  naam='mediaomvormer aanwezig?',
                                                  label='mediaomvormer aanwezig?',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.mediaomvormerAanwezig',
                                                  definitie='Definitie nog toe te voegen voor eigenschap mediaomvormer aanwezig?')

        self._merkEnTypeCamera = EMAttribuut(field=StringField,
                                             naam='merk en type camera',
                                             label='merk en type camera',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.merkEnTypeCamera',
                                             definitie='Definitie nog toe te voegen voor eigenschap merk en type camera')

        self._paalkastAanwezig = EMAttribuut(field=BooleanField,
                                             naam='paalkast aanwezig',
                                             label='paalkast aanwezig',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastAanwezig',
                                             definitie='Definitie nog toe te voegen voor eigenschap paalkast aanwezig')

        self._vertrekAanwezig = EMAttribuut(field=BooleanField,
                                            naam='vertrek aanwezig?',
                                            label='vertrek aanwezig?',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vertrekAanwezig',
                                            definitie='Definitie nog toe te voegen voor eigenschap vertrek aanwezig?')

    @property
    def wifiAntenneAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap WIFI antenne aanwezig"""
        return self._wifiAntenneAanwezig.waarde

    @wifiAntenneAanwezig.setter
    def wifiAntenneAanwezig(self, value):
        self._wifiAntenneAanwezig.set_waarde(value, owner=self)

    @property
    def datumNieuwVertrekGeplaatst(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuw vertrek geplaatst"""
        return self._datumNieuwVertrekGeplaatst.waarde

    @datumNieuwVertrekGeplaatst.setter
    def datumNieuwVertrekGeplaatst(self, value):
        self._datumNieuwVertrekGeplaatst.set_waarde(value, owner=self)

    @property
    def datumNieuweCamera(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe camera"""
        return self._datumNieuweCamera.waarde

    @datumNieuweCamera.setter
    def datumNieuweCamera(self, value):
        self._datumNieuweCamera.set_waarde(value, owner=self)

    @property
    def datumNieuweEncoder(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe encoder"""
        return self._datumNieuweEncoder.waarde

    @datumNieuweEncoder.setter
    def datumNieuweEncoder(self, value):
        self._datumNieuweEncoder.set_waarde(value, owner=self)

    @property
    def datumNieuweMediaomvormer(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe mediaomvormer"""
        return self._datumNieuweMediaomvormer.waarde

    @datumNieuweMediaomvormer.setter
    def datumNieuweMediaomvormer(self, value):
        self._datumNieuweMediaomvormer.set_waarde(value, owner=self)

    @property
    def encoderAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap encoder aanwezig?"""
        return self._encoderAanwezig.waarde

    @encoderAanwezig.setter
    def encoderAanwezig(self, value):
        self._encoderAanwezig.set_waarde(value, owner=self)

    @property
    def encoderInExterneKast(self):
        """Definitie nog toe te voegen voor eigenschap encoder in externe kast"""
        return self._encoderInExterneKast.waarde

    @encoderInExterneKast.setter
    def encoderInExterneKast(self, value):
        self._encoderInExterneKast.set_waarde(value, owner=self)

    @property
    def mediaomvormerAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap mediaomvormer aanwezig?"""
        return self._mediaomvormerAanwezig.waarde

    @mediaomvormerAanwezig.setter
    def mediaomvormerAanwezig(self, value):
        self._mediaomvormerAanwezig.set_waarde(value, owner=self)

    @property
    def merkEnTypeCamera(self):
        """Definitie nog toe te voegen voor eigenschap merk en type camera"""
        return self._merkEnTypeCamera.waarde

    @merkEnTypeCamera.setter
    def merkEnTypeCamera(self, value):
        self._merkEnTypeCamera.set_waarde(value, owner=self)

    @property
    def paalkastAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap paalkast aanwezig"""
        return self._paalkastAanwezig.waarde

    @paalkastAanwezig.setter
    def paalkastAanwezig(self, value):
        self._paalkastAanwezig.set_waarde(value, owner=self)

    @property
    def vertrekAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap vertrek aanwezig?"""
        return self._vertrekAanwezig.waarde

    @vertrekAanwezig.setter
    def vertrekAanwezig(self, value):
        self._vertrekAanwezig.set_waarde(value, owner=self)

