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

        self._ivsbBuitenGebruik = EMAttribuut(field=BooleanField,
                                              naam='IVSB buiten gebruik',
                                              label='IVSB buiten gebruik',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.ivsbBuitenGebruik',
                                              definitie='indien IVSB nutteloos is, kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering',
                                              owner=self)

        self._ledVerlichting = EMAttribuut(field=BooleanField,
                                           naam='LED verlichting',
                                           label='LED verlichting',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ledVerlichting',
                                           definitie='Definitie nog toe te voegen voor eigenschap LED verlichting',
                                           owner=self)

        self._vsaType = EMAttribuut(field=StringField,
                                    naam='VSA type',
                                    label='VSA type',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaType',
                                    definitie='keuzelijst elektromagnetisch, elektronisch, niet gekend',
                                    owner=self)

        self._aantalVsaLaagsteVermogenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                              naam='aantal VSA laagste vermogen vervangen',
                                                              label='aantal VSA laagste vermogen vervangen',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalVsaLaagsteVermogenVervangen',
                                                              definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn',
                                                              owner=self)

        self._aantalVsaVervangen = EMAttribuut(field=FloatOrDecimalField,
                                               naam='aantal VSA vervangen',
                                               label='aantal VSA vervangen',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalVsaVervangen',
                                               definitie='Definitie nog toe te voegen voor eigenschap aantal VSA vervangen',
                                               owner=self)

        self._aantalDeurtjesVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='aantal deurtjes vervangen',
                                                    label='aantal deurtjes vervangen',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalDeurtjesVervangen',
                                                    definitie='Definitie nog toe te voegen voor eigenschap aantal deurtjes vervangen',
                                                    owner=self)

        self._aantalLampen = EMAttribuut(field=FloatOrDecimalField,
                                         naam='aantal lampen',
                                         label='aantal lampen',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalLampen',
                                         definitie='Definitie nog toe te voegen voor eigenschap aantal lampen',
                                         owner=self)

        self._aantalLampenLaagsteVermogen = EMAttribuut(field=FloatOrDecimalField,
                                                        naam='aantal lampen laagste vermogen',
                                                        label='aantal lampen laagste vermogen',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalLampenLaagsteVermogen',
                                                        definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn',
                                                        owner=self)

        self._aantalLampenLaagsteVermogenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                                 naam='aantal lampen laagste vermogen vervangen',
                                                                 label='aantal lampen laagste vermogen vervangen',
                                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalLampenLaagsteVermogenVervangen',
                                                                 definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn',
                                                                 owner=self)

        self._aantalLampenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                  naam='aantal lampen vervangen',
                                                  label='aantal lampen vervangen',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalLampenVervangen',
                                                  definitie='Definitie nog toe te voegen voor eigenschap aantal lampen vervangen',
                                                  owner=self)

        self._aantalOntstekersLaagsteVermogenVerv = EMAttribuut(field=FloatOrDecimalField,
                                                                naam='aantal ontstekers laagste vermogen verv',
                                                                label='aantal ontstekers laagste vermogen verv',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalOntstekersLaagsteVermogenVerv',
                                                                definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn',
                                                                owner=self)

        self._aantalOntstekersVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='aantal ontstekers vervangen',
                                                      label='aantal ontstekers vervangen',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.aantalOntstekersVervangen',
                                                      definitie='Definitie nog toe te voegen voor eigenschap aantal ontstekers vervangen',
                                                      owner=self)

        self._afmeting = EMAttribuut(field=StringField,
                                     naam='afmeting',
                                     label='afmeting',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.afmeting',
                                     definitie='tekstveld voor het bijhouden van de afmeting',
                                     owner=self)

        self._anderTypeBord = EMAttribuut(field=StringField,
                                          naam='ander type bord',
                                          label='ander type bord',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.anderTypeBord',
                                          definitie='Definitie nog toe te voegen voor eigenschap ander type bord',
                                          owner=self)

        self._datumNieuweIvsb = EMAttribuut(field=DateField,
                                            naam='datum nieuwe IVSB',
                                            label='datum nieuwe IVSB',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.datumNieuweIvsb',
                                            definitie='datum waarop IVSB geplaatst is',
                                            owner=self)

        self._gecombineerdMetAnderBord = EMAttribuut(field=BooleanField,
                                                     naam='gecombineerd met ander bord',
                                                     label='gecombineerd met ander bord',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.gecombineerdMetAnderBord',
                                                     definitie='aanduiden als er aan/op het bord een vsb of retroreflecterend stuk bevestigd is',
                                                     owner=self)

        self._isolatieweerstand = EMAttribuut(field=FloatOrDecimalField,
                                              naam='isolatieweerstand',
                                              label='isolatieweerstand',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.isolatieweerstand',
                                              definitie='Definitie nog toe te voegen voor eigenschap isolatieweerstand',
                                              owner=self)

        self._lampType = EMAttribuut(field=StringField,
                                     naam='lamp type',
                                     label='lamp type',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lampType',
                                     definitie='Lijst lamptypes',
                                     owner=self)

        self._lampTypeLaagsteVermogen = EMAttribuut(field=StringField,
                                                    naam='lamp type laagste vermogen',
                                                    label='lamp type laagste vermogen',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.lampTypeLaagsteVermogen',
                                                    definitie='afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn',
                                                    owner=self)

        self._nogTeHerstellenOpmerkingen = EMAttribuut(field=StringField,
                                                       naam='nog te herstellen/opmerkingen',
                                                       label='nog te herstellen/opmerkingen',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.nogTeHerstellenOpmerkingen',
                                                       definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                       owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

        self._onderhoudUitgevoerd = EMAttribuut(field=StringField,
                                                naam='onderhoud uitgevoerd',
                                                label='onderhoud uitgevoerd',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#IVSB.onderhoudUitgevoerd',
                                                definitie='Definitie nog toe te voegen voor eigenschap onderhoud uitgevoerd',
                                                owner=self)

        self._opmerkingElektrischeApparatuur = EMAttribuut(field=StringField,
                                                           naam='opmerking elektrische apparatuur',
                                                           label='opmerking elektrische apparatuur',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.opmerkingElektrischeApparatuur',
                                                           definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                           owner=self)

        self._opmerkingInventarisIvsb = EMAttribuut(field=StringField,
                                                    naam='opmerking inventaris IVSB',
                                                    label='opmerking inventaris IVSB',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.opmerkingInventarisIvsb',
                                                    definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                    owner=self)

        self._opmerkingToestandIvsb = EMAttribuut(field=StringField,
                                                  naam='opmerking toestand IVSB',
                                                  label='opmerking toestand IVSB',
                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.opmerkingToestandIvsb',
                                                  definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                  owner=self)

        self._redenIvsbBuitenGebruik = EMAttribuut(field=StringField,
                                                   naam='reden IVSB buiten gebruik',
                                                   label='reden IVSB buiten gebruik',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.redenIvsbBuitenGebruik',
                                                   definitie='Definitie nog toe te voegen voor eigenschap reden IVSB buiten gebruik',
                                                   owner=self)

        self._tekstEnSymbolen = EMAttribuut(field=StringField,
                                            naam='tekst en symbolen',
                                            label='tekst en symbolen',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.tekstEnSymbolen',
                                            definitie='tekstveld waar opschrift van bord bijgehouden kan worden',
                                            owner=self)

        self._toestandIvsb = EMAttribuut(field=StringField,
                                         naam='toestand IVSB',
                                         label='toestand IVSB',
                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.toestandIvsb',
                                         definitie='Definitie nog toe te voegen voor eigenschap toestand IVSB',
                                         owner=self)

        self._toestandBeugelsBevestigingsmiddelen = EMAttribuut(field=StringField,
                                                                naam='toestand beugels/bevestigingsmiddelen',
                                                                label='toestand beugels/bevestigingsmiddelen',
                                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.toestandBeugelsBevestigingsmiddelen',
                                                                definitie='Definitie nog toe te voegen voor eigenschap toestand beugels/bevestigingsmiddelen',
                                                                owner=self)

        self._toestandDeurtjeSluitingssysteem = EMAttribuut(field=StringField,
                                                            naam='toestand deurtje/sluitingssysteem',
                                                            label='toestand deurtje/sluitingssysteem',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.toestandDeurtjeSluitingssysteem',
                                                            definitie='Definitie nog toe te voegen voor eigenschap toestand deurtje/sluitingssysteem',
                                                            owner=self)

        self._toestandElektrischeApparatuur = EMAttribuut(field=StringField,
                                                          naam='toestand elektrische apparatuur',
                                                          label='toestand elektrische apparatuur',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.toestandElektrischeApparatuur',
                                                          definitie='Definitie nog toe te voegen voor eigenschap toestand elektrische apparatuur',
                                                          owner=self)

        self._typeIvsb = EMAttribuut(field=StringField,
                                     naam='type IVSB',
                                     label='type IVSB',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#IVSB.typeIvsb',
                                     definitie='Definitie nog toe te voegen voor eigenschap type IVSB',
                                     owner=self)

        self._typeOnderhoud = EMAttribuut(field=StringField,
                                          naam='type onderhoud',
                                          label='type onderhoud',
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.typeOnderhoud',
                                          definitie='Definitie nog toe te voegen voor eigenschap type onderhoud',
                                          owner=self)

        self._waterdichtheidKabelinvoer = EMAttribuut(field=StringField,
                                                      naam='waterdichtheid kabelinvoer',
                                                      label='waterdichtheid kabelinvoer',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.waterdichtheidKabelinvoer',
                                                      definitie='Definitie nog toe te voegen voor eigenschap waterdichtheid kabelinvoer',
                                                      owner=self)

        self._werkingIvsb = EMAttribuut(field=StringField,
                                        naam='werking IVSB',
                                        label='werking IVSB',
                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#IVSB.werkingIvsb',
                                        definitie='Definitie nog toe te voegen voor eigenschap werking IVSB',
                                        owner=self)

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
    def aantalVsaLaagsteVermogenVervangen(self):
        """afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn"""
        return self._aantalVsaLaagsteVermogenVervangen.waarde

    @aantalVsaLaagsteVermogenVervangen.setter
    def aantalVsaLaagsteVermogenVervangen(self, value):
        self._aantalVsaLaagsteVermogenVervangen.set_waarde(value, owner=self)

    @property
    def aantalVsaVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal VSA vervangen"""
        return self._aantalVsaVervangen.waarde

    @aantalVsaVervangen.setter
    def aantalVsaVervangen(self, value):
        self._aantalVsaVervangen.set_waarde(value, owner=self)

    @property
    def aantalDeurtjesVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal deurtjes vervangen"""
        return self._aantalDeurtjesVervangen.waarde

    @aantalDeurtjesVervangen.setter
    def aantalDeurtjesVervangen(self, value):
        self._aantalDeurtjesVervangen.set_waarde(value, owner=self)

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
    def aantalLampenLaagsteVermogenVervangen(self):
        """afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn"""
        return self._aantalLampenLaagsteVermogenVervangen.waarde

    @aantalLampenLaagsteVermogenVervangen.setter
    def aantalLampenLaagsteVermogenVervangen(self, value):
        self._aantalLampenLaagsteVermogenVervangen.set_waarde(value, owner=self)

    @property
    def aantalLampenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal lampen vervangen"""
        return self._aantalLampenVervangen.waarde

    @aantalLampenVervangen.setter
    def aantalLampenVervangen(self, value):
        self._aantalLampenVervangen.set_waarde(value, owner=self)

    @property
    def aantalOntstekersLaagsteVermogenVerv(self):
        """afhankelijk veld, dient enkel getoond te worden als er 2 lamptypes aanwezig zijn"""
        return self._aantalOntstekersLaagsteVermogenVerv.waarde

    @aantalOntstekersLaagsteVermogenVerv.setter
    def aantalOntstekersLaagsteVermogenVerv(self, value):
        self._aantalOntstekersLaagsteVermogenVerv.set_waarde(value, owner=self)

    @property
    def aantalOntstekersVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal ontstekers vervangen"""
        return self._aantalOntstekersVervangen.waarde

    @aantalOntstekersVervangen.setter
    def aantalOntstekersVervangen(self, value):
        self._aantalOntstekersVervangen.set_waarde(value, owner=self)

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
    def isolatieweerstand(self):
        """Definitie nog toe te voegen voor eigenschap isolatieweerstand"""
        return self._isolatieweerstand.waarde

    @isolatieweerstand.setter
    def isolatieweerstand(self, value):
        self._isolatieweerstand.set_waarde(value, owner=self)

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
    def nogTeHerstellenOpmerkingen(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._nogTeHerstellenOpmerkingen.waarde

    @nogTeHerstellenOpmerkingen.setter
    def nogTeHerstellenOpmerkingen(self, value):
        self._nogTeHerstellenOpmerkingen.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

    @property
    def onderhoudUitgevoerd(self):
        """Definitie nog toe te voegen voor eigenschap onderhoud uitgevoerd"""
        return self._onderhoudUitgevoerd.waarde

    @onderhoudUitgevoerd.setter
    def onderhoudUitgevoerd(self, value):
        self._onderhoudUitgevoerd.set_waarde(value, owner=self)

    @property
    def opmerkingElektrischeApparatuur(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingElektrischeApparatuur.waarde

    @opmerkingElektrischeApparatuur.setter
    def opmerkingElektrischeApparatuur(self, value):
        self._opmerkingElektrischeApparatuur.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisIvsb(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisIvsb.waarde

    @opmerkingInventarisIvsb.setter
    def opmerkingInventarisIvsb(self, value):
        self._opmerkingInventarisIvsb.set_waarde(value, owner=self)

    @property
    def opmerkingToestandIvsb(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingToestandIvsb.waarde

    @opmerkingToestandIvsb.setter
    def opmerkingToestandIvsb(self, value):
        self._opmerkingToestandIvsb.set_waarde(value, owner=self)

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
    def toestandIvsb(self):
        """Definitie nog toe te voegen voor eigenschap toestand IVSB"""
        return self._toestandIvsb.waarde

    @toestandIvsb.setter
    def toestandIvsb(self, value):
        self._toestandIvsb.set_waarde(value, owner=self)

    @property
    def toestandBeugelsBevestigingsmiddelen(self):
        """Definitie nog toe te voegen voor eigenschap toestand beugels/bevestigingsmiddelen"""
        return self._toestandBeugelsBevestigingsmiddelen.waarde

    @toestandBeugelsBevestigingsmiddelen.setter
    def toestandBeugelsBevestigingsmiddelen(self, value):
        self._toestandBeugelsBevestigingsmiddelen.set_waarde(value, owner=self)

    @property
    def toestandDeurtjeSluitingssysteem(self):
        """Definitie nog toe te voegen voor eigenschap toestand deurtje/sluitingssysteem"""
        return self._toestandDeurtjeSluitingssysteem.waarde

    @toestandDeurtjeSluitingssysteem.setter
    def toestandDeurtjeSluitingssysteem(self, value):
        self._toestandDeurtjeSluitingssysteem.set_waarde(value, owner=self)

    @property
    def toestandElektrischeApparatuur(self):
        """Definitie nog toe te voegen voor eigenschap toestand elektrische apparatuur"""
        return self._toestandElektrischeApparatuur.waarde

    @toestandElektrischeApparatuur.setter
    def toestandElektrischeApparatuur(self, value):
        self._toestandElektrischeApparatuur.set_waarde(value, owner=self)

    @property
    def typeIvsb(self):
        """Definitie nog toe te voegen voor eigenschap type IVSB"""
        return self._typeIvsb.waarde

    @typeIvsb.setter
    def typeIvsb(self, value):
        self._typeIvsb.set_waarde(value, owner=self)

    @property
    def typeOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap type onderhoud"""
        return self._typeOnderhoud.waarde

    @typeOnderhoud.setter
    def typeOnderhoud(self, value):
        self._typeOnderhoud.set_waarde(value, owner=self)

    @property
    def waterdichtheidKabelinvoer(self):
        """Definitie nog toe te voegen voor eigenschap waterdichtheid kabelinvoer"""
        return self._waterdichtheidKabelinvoer.waarde

    @waterdichtheidKabelinvoer.setter
    def waterdichtheidKabelinvoer(self, value):
        self._waterdichtheidKabelinvoer.set_waarde(value, owner=self)

    @property
    def werkingIvsb(self):
        """Definitie nog toe te voegen voor eigenschap werking IVSB"""
        return self._werkingIvsb.waarde

    @werkingIvsb.setter
    def werkingIvsb(self, value):
        self._werkingIvsb.set_waarde(value, owner=self)

