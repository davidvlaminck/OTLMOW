# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class IVSB(EMObject):
    """INWENDIG VERLICHTE SIGNALISATIEBORDEN"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#IVSB'
    label = 'Inwendig verlichte signalisatieborden'

    def __init__(self):
        super().__init__()

        self._2TypesLampenAanwezig = EMAttribuut(field=BooleanField,
                                                 naam='2 types lampen aanwezig',
                                                 label='2 types lampen aanwezig',
                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.2TypesLampenAanwezig',
                                                 definitie='selecteren indien er 2 types lampen in het IVS bord aanwezig zijn')

        self._ivsbBuitenGebruik = EMAttribuut(field=BooleanField,
                                              naam='IVSB buiten gebruik',
                                              label='IVSB buiten gebruik',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.ivsbBuitenGebruik',
                                              definitie='indien IVSB nutteloos is, kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering')

        self._ledVerlichting = EMAttribuut(field=BooleanField,
                                           naam='LED verlichting',
                                           label='LED verlichting',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ledVerlichting',
                                           definitie='Definitie nog toe te voegen voor eigenschap LED verlichting')

        self._vsaType = EMAttribuut(field=StringField,
                                    naam='VSA type',
                                    label='VSA type',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaType',
                                    definitie='keuzelijst elektromagnetisch, elektronisch, niet gekend')

        self._aantalLampen = EMAttribuut(field=FloatOrDecimalField,
                                         naam='aantal lampen',
                                         label='aantal lampen',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalLampen',
                                         definitie='Definitie nog toe te voegen voor eigenschap aantal lampen')

        self._aantalLampenLaagsteVermogen = EMAttribuut(field=FloatOrDecimalField,
                                                        naam='aantal lampen laagste vermogen',
                                                        label='aantal lampen laagste vermogen',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalLampenLaagsteVermogen',
                                                        definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn')

        self._afmeting = EMAttribuut(field=StringField,
                                     naam='afmeting',
                                     label='afmeting',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.afmeting',
                                     definitie='tekstveld voor het bijhouden van de afmeting')

        self._anderTypeBord = EMAttribuut(field=StringField,
                                          naam='ander type bord',
                                          label='ander type bord',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.anderTypeBord',
                                          definitie='Definitie nog toe te voegen voor eigenschap ander type bord')

        self._datumNieuweIvsb = EMAttribuut(field=DateField,
                                            naam='datum nieuwe IVSB',
                                            label='datum nieuwe IVSB',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.datumNieuweIvsb',
                                            definitie='datum waarop IVSB geplaatst is')

        self._gecombineerdMetAnderBord = EMAttribuut(field=BooleanField,
                                                     naam='gecombineerd met ander bord',
                                                     label='gecombineerd met ander bord',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.gecombineerdMetAnderBord',
                                                     definitie='aanduiden als er aan/op het bord een vsb of retroreflecterend stuk bevestigd is')

        self._lampType = EMAttribuut(field=StringField,
                                     naam='lamp type',
                                     label='lamp type',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lampType',
                                     definitie='Lijst lamptypes')

        self._lampTypeLaagsteVermogen = EMAttribuut(field=StringField,
                                                    naam='lamp type laagste vermogen',
                                                    label='lamp type laagste vermogen',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.lampTypeLaagsteVermogen',
                                                    definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn')

        self._opmerkingInventarisIvsb = EMAttribuut(field=StringField,
                                                    naam='opmerking inventaris IVSB',
                                                    label='opmerking inventaris IVSB',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.opmerkingInventarisIvsb',
                                                    definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._redenIvsbBuitenGebruik = EMAttribuut(field=StringField,
                                                   naam='reden IVSB buiten gebruik',
                                                   label='reden IVSB buiten gebruik',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.redenIvsbBuitenGebruik',
                                                   definitie='Definitie nog toe te voegen voor eigenschap reden IVSB buiten gebruik')

        self._tekstEnSymbolen = EMAttribuut(field=StringField,
                                            naam='tekst en symbolen',
                                            label='tekst en symbolen',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.tekstEnSymbolen',
                                            definitie='tekstveld waar opschrift van bord bijgehouden kan worden')

        self._typeIvsb = EMAttribuut(field=StringField,
                                     naam='type IVSB',
                                     label='type IVSB',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.typeIvsb',
                                     definitie='Definitie nog toe te voegen voor eigenschap type IVSB')

    @property
    def 2TypesLampenAanwezig(self):
        """selecteren indien er 2 types lampen in het IVS bord aanwezig zijn"""
        return self._2TypesLampenAanwezig.waarde

    @2TypesLampenAanwezig.setter
    def 2TypesLampenAanwezig(self, value):
        self._2TypesLampenAanwezig.set_waarde(value, owner=self)

    @property
    def ivsbBuitenGebruik(self):
        """indien IVSB nutteloos is, kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering"""
        return self._ivsbBuitenGebruik.waarde

    @ivsbBuitenGebruik.setter
    def ivsbBuitenGebruik(self, value):
        self._ivsbBuitenGebruik.set_waarde(value, owner=self)

    @property
    def ledVerlichting(self):
        """Definitie nog toe te voegen voor eigenschap LED verlichting"""
        return self._ledVerlichting.waarde

    @ledVerlichting.setter
    def ledVerlichting(self, value):
        self._ledVerlichting.set_waarde(value, owner=self)

    @property
    def vsaType(self):
        """keuzelijst elektromagnetisch, elektronisch, niet gekend"""
        return self._vsaType.waarde

    @vsaType.setter
    def vsaType(self, value):
        self._vsaType.set_waarde(value, owner=self)

    @property
    def aantalLampen(self):
        """Definitie nog toe te voegen voor eigenschap aantal lampen"""
        return self._aantalLampen.waarde

    @aantalLampen.setter
    def aantalLampen(self, value):
        self._aantalLampen.set_waarde(value, owner=self)

    @property
    def aantalLampenLaagsteVermogen(self):
        """afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn"""
        return self._aantalLampenLaagsteVermogen.waarde

    @aantalLampenLaagsteVermogen.setter
    def aantalLampenLaagsteVermogen(self, value):
        self._aantalLampenLaagsteVermogen.set_waarde(value, owner=self)

    @property
    def afmeting(self):
        """tekstveld voor het bijhouden van de afmeting"""
        return self._afmeting.waarde

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def anderTypeBord(self):
        """Definitie nog toe te voegen voor eigenschap ander type bord"""
        return self._anderTypeBord.waarde

    @anderTypeBord.setter
    def anderTypeBord(self, value):
        self._anderTypeBord.set_waarde(value, owner=self)

    @property
    def datumNieuweIvsb(self):
        """datum waarop IVSB geplaatst is"""
        return self._datumNieuweIvsb.waarde

    @datumNieuweIvsb.setter
    def datumNieuweIvsb(self, value):
        self._datumNieuweIvsb.set_waarde(value, owner=self)

    @property
    def gecombineerdMetAnderBord(self):
        """aanduiden als er aan/op het bord een vsb of retroreflecterend stuk bevestigd is"""
        return self._gecombineerdMetAnderBord.waarde

    @gecombineerdMetAnderBord.setter
    def gecombineerdMetAnderBord(self, value):
        self._gecombineerdMetAnderBord.set_waarde(value, owner=self)

    @property
    def lampType(self):
        """Lijst lamptypes"""
        return self._lampType.waarde

    @lampType.setter
    def lampType(self, value):
        self._lampType.set_waarde(value, owner=self)

    @property
    def lampTypeLaagsteVermogen(self):
        """afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn"""
        return self._lampTypeLaagsteVermogen.waarde

    @lampTypeLaagsteVermogen.setter
    def lampTypeLaagsteVermogen(self, value):
        self._lampTypeLaagsteVermogen.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisIvsb(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisIvsb.waarde

    @opmerkingInventarisIvsb.setter
    def opmerkingInventarisIvsb(self, value):
        self._opmerkingInventarisIvsb.set_waarde(value, owner=self)

    @property
    def redenIvsbBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden IVSB buiten gebruik"""
        return self._redenIvsbBuitenGebruik.waarde

    @redenIvsbBuitenGebruik.setter
    def redenIvsbBuitenGebruik(self, value):
        self._redenIvsbBuitenGebruik.set_waarde(value, owner=self)

    @property
    def tekstEnSymbolen(self):
        """tekstveld waar opschrift van bord bijgehouden kan worden"""
        return self._tekstEnSymbolen.waarde

    @tekstEnSymbolen.setter
    def tekstEnSymbolen(self, value):
        self._tekstEnSymbolen.set_waarde(value, owner=self)

    @property
    def typeIvsb(self):
        """Definitie nog toe te voegen voor eigenschap type IVSB"""
        return self._typeIvsb.waarde

    @typeIvsb.setter
    def typeIvsb(self, value):
        self._typeIvsb.set_waarde(value, owner=self)

