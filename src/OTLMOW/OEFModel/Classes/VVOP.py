# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class VVOP(EMObject):
    """Verlichte voetgangersoversteekplaats"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VVOP'
    label = 'Verlichte voetgangersoversteekplaats'

    def __init__(self):
        super().__init__()

        self._ledVerlichting = EMAttribuut(field=BooleanField,
                                           naam='LED verlichting',
                                           label='LED verlichting',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ledVerlichting',
                                           definitie='Definitie nog toe te voegen voor eigenschap LED verlichting')

        self._ralKleur = EMAttribuut(field=StringField,
                                     naam='RAL kleur',
                                     label='RAL kleur',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.ralKleur',
                                     definitie='Definitie nog toe te voegen voor eigenschap RAL kleur')

        self._vsaType = EMAttribuut(field=StringField,
                                    naam='VSA type',
                                    label='VSA type',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaType',
                                    definitie='keuzelijst elektromagnetisch, elektronisch, niet gekend')

        self._verticaleSignalisatieOversteek = EMAttribuut(field=StringField,
                                                           naam='Verticale signalisatie thv oversteek',
                                                           label='Verticale signalisatie thv oversteek',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.verticaleSignalisatieOversteek',
                                                           definitie='Verticale signalisatie thv oversteek')

        self._aantalArmen = EMAttribuut(field=StringField,
                                        naam='aantal armen',
                                        label='aantal armen',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.aantalArmen',
                                        definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast \'M\', \'MS\', \'B\',\'BS\', \'K\' of \'KS\' dan 0,1, 2,3 of 4. Anders altijd 0.")

        self._aantalKlemmenblokkenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                          naam='aantal klemmenblokken vervangen',
                                                          label='aantal klemmenblokken vervangen',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalKlemmenblokkenVervangen',
                                                          definitie='Definitie nog toe te voegen voor eigenschap aantal klemmenblokken vervangen')

        self._aantalVerlichtingstoestellen = EMAttribuut(field=FloatOrDecimalField,
                                                         naam='aantal verlichtingstoestellen',
                                                         label='aantal verlichtingstoestellen',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalVerlichtingstoestellen',
                                                         definitie='Definitie nog toe te voegen voor eigenschap aantal verlichtingstoestellen')

        self._aantalZekeringenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='aantal zekeringen vervangen',
                                                      label='aantal zekeringen vervangen',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalZekeringenVervangen',
                                                      definitie='Definitie nog toe te voegen voor eigenschap aantal zekeringen vervangen')

        self._armlengteVVOP = EMAttribuut(field=StringField,
                                          naam='armlengteVVOP',
                                          label='armlengteVVOP',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.armlengteVVOP',
                                          definitie='armlengteVVOP')

        self._biflash = EMAttribuut(field=BooleanField,
                                    naam='biflash',
                                    label='biflash',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.biflash',
                                    definitie='biflash')

        self._datumLichtmastGeschilderd = EMAttribuut(field=DateField,
                                                      naam='datum lichtmast geschilderd',
                                                      label='datum lichtmast geschilderd',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.datumLichtmastGeschilderd',
                                                      definitie='datum waarop lichtmast laatste keer is geschilderd')

        self._deurtjeVervangen = EMAttribuut(field=BooleanField,
                                             naam='deurtje vervangen',
                                             label='deurtje vervangen',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#VPLMast.deurtjeVervangen',
                                             definitie='Definitie nog toe te voegen voor eigenschap deurtje vervangen')

        self._directGevaar = EMAttribuut(field=BooleanField,
                                         naam='direct gevaar',
                                         label='direct gevaar',
                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.directGevaar',
                                         definitie='Definitie nog toe te voegen voor eigenschap direct gevaar')

        self._externeRoestvorming = EMAttribuut(field=StringField,
                                                naam='externe roestvorming',
                                                label='externe roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.externeRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._interneRoestvorming = EMAttribuut(field=StringField,
                                                naam='interne roestvorming',
                                                label='interne roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.interneRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._kleurtemperatuurLed = EMAttribuut(field=StringField,
                                                naam='kleurtemperatuur LED',
                                                label='kleurtemperatuur LED',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.kleurtemperatuurLed',
                                                definitie='Definitie nog toe te voegen voor eigenschap kleurtemperatuur LED')

        self._leverancier = EMAttribuut(field=StringField,
                                        naam='leverancier',
                                        label='leverancier',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.leverancier',
                                        definitie='keuzelijst (Baert, PetitJean, Safety Products, andere, niet gekend)')

        self._lichtmastBuitenGebruik = EMAttribuut(field=BooleanField,
                                                   naam='lichtmast buiten gebruik',
                                                   label='lichtmast buiten gebruik',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.lichtmastBuitenGebruik',
                                                   definitie='indien lichtmast nutteloos is (geen lichtpunt meer), kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering')

        self._lichtpunthoogteVVOP = EMAttribuut(field=StringField,
                                                naam='lichtpunthoogteVVOP',
                                                label='lichtpunthoogteVVOP',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.lichtpunthoogteVVOP',
                                                definitie='lichtpunthoogte VVOP')

        self._nummerLeesbaar = EMAttribuut(field=StringField,
                                           naam='nummer leesbaar',
                                           label='nummer leesbaar',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.nummerLeesbaar',
                                           definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._nummerVoedingskring = EMAttribuut(field=StringField,
                                                naam='nummer voedingskring',
                                                label='nummer voedingskring',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.nummerVoedingskring',
                                                definitie='identificatie voedingskring : tekstveld om variatie provincies op te vangen : kring A, B, C, ... of  kring 1, 2, 9, ... of ...')

        self._punctueleVerlichtingLichtbron = EMAttribuut(field=StringField,
                                                          naam='punctuele verlichting lichtbron',
                                                          label='punctuele verlichting lichtbron',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.punctueleVerlichtingLichtbron',
                                                          definitie='punctuele verlichting lichtbron')

        self._verlichtingToestelMerkEnType = EMAttribuut(field=StringField,
                                                         naam='punctuele verlichting toestel merk en type',
                                                         label='punctuele verlichting toestel merk en type',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.verlichtingToestelMerkEnType',
                                                         definitie='punctuele verlichting toestel merk en type')

        self._redenLichtmastBuitenGebruik = EMAttribuut(field=StringField,
                                                        naam='reden lichtmast buiten gebruik',
                                                        label='reden lichtmast buiten gebruik',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.redenLichtmastBuitenGebruik',
                                                        definitie='afhankelijke eigenschap die enkel moet getoond worden indien waarde "buiten gebruik" ja. keuzelijst (niet van toepassing, normale slijtage, averij, andere)')

        self._risicovollePaal = EMAttribuut(field=BooleanField,
                                            naam='risicovolle paal',
                                            label='risicovolle paal',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.risicovollePaal',
                                            definitie='ja als paal extra aandacht vraagt zie inspectiehandboek voor definitie : te bepalen door projectingenieur/toezichter dus niet wijzigbaar voor aannemer')

        self._toestandBouten = EMAttribuut(field=StringField,
                                           naam='toestand bouten',
                                           label='toestand bouten',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPLMast.toestandBouten',
                                           definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandDeurtje = EMAttribuut(field=StringField,
                                            naam='toestand deurtje',
                                            label='toestand deurtje',
                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPLMast.toestandDeurtje',
                                            definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandFundering = EMAttribuut(field=StringField,
                                              naam='toestand fundering',
                                              label='toestand fundering',
                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.toestandFundering',
                                              definitie='Definitie nog toe te voegen voor eigenschap toestand fundering')

        self._toestandPaal = EMAttribuut(field=StringField,
                                         naam='toestand paal',
                                         label='toestand paal',
                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPLMast.toestandPaal',
                                         definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandVerlichtingstoestellen = EMAttribuut(field=StringField,
                                                           naam='toestand verlichtingstoestellen',
                                                           label='toestand verlichtingstoestellen',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.toestandVerlichtingstoestellen',
                                                           definitie='keuzelijst (OK, OK met opmerkingen, Ã©Ã©n of meer toestellen of lampen defect, niet gekend)')

        self._toestelkleur = EMAttribuut(field=StringField,
                                         naam='toestelkleur',
                                         label='toestelkleur',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VVOP.toestelkleur',
                                         definitie='toestelkleur in RAL')

        self._verlichtingOpstelling = EMAttribuut(field=StringField,
                                                  naam='verlichting opstelling',
                                                  label='verlichting opstelling',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingOpstelling',
                                                  definitie='Opstelling van de verlichting (zijberm of middenberm)')

        self._verlichtingsniveauLed = EMAttribuut(field=StringField,
                                                  naam='verlichtingsniveau LED',
                                                  label='verlichtingsniveau LED',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingsniveauLed',
                                                  definitie='Definitie nog toe te voegen voor eigenschap verlichtingsniveau LED')

        self._verlichtingstoestelSysteemvermogen = EMAttribuut(field=FloatOrDecimalField,
                                                               naam='verlichtingstoestel systeemvermogen',
                                                               label='verlichtingstoestel systeemvermogen',
                                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstoestelSysteemvermogen',
                                                               definitie='vermogen (in Watt) van het verlichtingstoestel')

        self._verlichtingstype = EMAttribuut(field=StringField,
                                             naam='verlichtingstype',
                                             label='verlichtingstype',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstype',
                                             definitie='keuzelijst met types verlichting (doorlopende straatverlichting, rotonde verlichting, punctuele verlichting, projector, tunnelverlichting)')

        self._vsaSperfilter = EMAttribuut(field=BooleanField,
                                          naam='vsa sperfilter',
                                          label='vsa sperfilter',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaSperfilter',
                                          definitie='ja als sperfilter op vsa')

    @property
    def ledVerlichting(self):
        """Definitie nog toe te voegen voor eigenschap LED verlichting"""
        return self._ledVerlichting.waarde

    @ledVerlichting.setter
    def ledVerlichting(self, value):
        self._ledVerlichting.set_waarde(value, owner=self)

    @property
    def ralKleur(self):
        """Definitie nog toe te voegen voor eigenschap RAL kleur"""
        return self._ralKleur.waarde

    @ralKleur.setter
    def ralKleur(self, value):
        self._ralKleur.set_waarde(value, owner=self)

    @property
    def vsaType(self):
        """keuzelijst elektromagnetisch, elektronisch, niet gekend"""
        return self._vsaType.waarde

    @vsaType.setter
    def vsaType(self, value):
        self._vsaType.set_waarde(value, owner=self)

    @property
    def verticaleSignalisatieOversteek(self):
        """Verticale signalisatie thv oversteek"""
        return self._verticaleSignalisatieOversteek.waarde

    @verticaleSignalisatieOversteek.setter
    def verticaleSignalisatieOversteek(self, value):
        self._verticaleSignalisatieOversteek.set_waarde(value, owner=self)

    @property
    def aantalArmen(self):
        """keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast \'M\', \'MS\', \'B\',\'BS\', \'K\' of \'KS\' dan 0,1, 2,3 of 4. Anders altijd 0."""
        return self._aantalArmen.waarde

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def aantalKlemmenblokkenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal klemmenblokken vervangen"""
        return self._aantalKlemmenblokkenVervangen.waarde

    @aantalKlemmenblokkenVervangen.setter
    def aantalKlemmenblokkenVervangen(self, value):
        self._aantalKlemmenblokkenVervangen.set_waarde(value, owner=self)

    @property
    def aantalVerlichtingstoestellen(self):
        """Definitie nog toe te voegen voor eigenschap aantal verlichtingstoestellen"""
        return self._aantalVerlichtingstoestellen.waarde

    @aantalVerlichtingstoestellen.setter
    def aantalVerlichtingstoestellen(self, value):
        self._aantalVerlichtingstoestellen.set_waarde(value, owner=self)

    @property
    def aantalZekeringenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal zekeringen vervangen"""
        return self._aantalZekeringenVervangen.waarde

    @aantalZekeringenVervangen.setter
    def aantalZekeringenVervangen(self, value):
        self._aantalZekeringenVervangen.set_waarde(value, owner=self)

    @property
    def armlengteVVOP(self):
        """armlengteVVOP"""
        return self._armlengteVVOP.waarde

    @armlengteVVOP.setter
    def armlengteVVOP(self, value):
        self._armlengteVVOP.set_waarde(value, owner=self)

    @property
    def biflash(self):
        """biflash"""
        return self._biflash.waarde

    @biflash.setter
    def biflash(self, value):
        self._biflash.set_waarde(value, owner=self)

    @property
    def datumLichtmastGeschilderd(self):
        """datum waarop lichtmast laatste keer is geschilderd"""
        return self._datumLichtmastGeschilderd.waarde

    @datumLichtmastGeschilderd.setter
    def datumLichtmastGeschilderd(self, value):
        self._datumLichtmastGeschilderd.set_waarde(value, owner=self)

    @property
    def deurtjeVervangen(self):
        """Definitie nog toe te voegen voor eigenschap deurtje vervangen"""
        return self._deurtjeVervangen.waarde

    @deurtjeVervangen.setter
    def deurtjeVervangen(self, value):
        self._deurtjeVervangen.set_waarde(value, owner=self)

    @property
    def directGevaar(self):
        """Definitie nog toe te voegen voor eigenschap direct gevaar"""
        return self._directGevaar.waarde

    @directGevaar.setter
    def directGevaar(self, value):
        self._directGevaar.set_waarde(value, owner=self)

    @property
    def externeRoestvorming(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._externeRoestvorming.waarde

    @externeRoestvorming.setter
    def externeRoestvorming(self, value):
        self._externeRoestvorming.set_waarde(value, owner=self)

    @property
    def interneRoestvorming(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._interneRoestvorming.waarde

    @interneRoestvorming.setter
    def interneRoestvorming(self, value):
        self._interneRoestvorming.set_waarde(value, owner=self)

    @property
    def kleurtemperatuurLed(self):
        """Definitie nog toe te voegen voor eigenschap kleurtemperatuur LED"""
        return self._kleurtemperatuurLed.waarde

    @kleurtemperatuurLed.setter
    def kleurtemperatuurLed(self, value):
        self._kleurtemperatuurLed.set_waarde(value, owner=self)

    @property
    def leverancier(self):
        """keuzelijst (Baert, PetitJean, Safety Products, andere, niet gekend)"""
        return self._leverancier.waarde

    @leverancier.setter
    def leverancier(self, value):
        self._leverancier.set_waarde(value, owner=self)

    @property
    def lichtmastBuitenGebruik(self):
        """indien lichtmast nutteloos is (geen lichtpunt meer), kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering"""
        return self._lichtmastBuitenGebruik.waarde

    @lichtmastBuitenGebruik.setter
    def lichtmastBuitenGebruik(self, value):
        self._lichtmastBuitenGebruik.set_waarde(value, owner=self)

    @property
    def lichtpunthoogteVVOP(self):
        """lichtpunthoogte VVOP"""
        return self._lichtpunthoogteVVOP.waarde

    @lichtpunthoogteVVOP.setter
    def lichtpunthoogteVVOP(self, value):
        self._lichtpunthoogteVVOP.set_waarde(value, owner=self)

    @property
    def nummerLeesbaar(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._nummerLeesbaar.waarde

    @nummerLeesbaar.setter
    def nummerLeesbaar(self, value):
        self._nummerLeesbaar.set_waarde(value, owner=self)

    @property
    def nummerVoedingskring(self):
        """identificatie voedingskring : tekstveld om variatie provincies op te vangen : kring A, B, C, ... of  kring 1, 2, 9, ... of ..."""
        return self._nummerVoedingskring.waarde

    @nummerVoedingskring.setter
    def nummerVoedingskring(self, value):
        self._nummerVoedingskring.set_waarde(value, owner=self)

    @property
    def punctueleVerlichtingLichtbron(self):
        """punctuele verlichting lichtbron"""
        return self._punctueleVerlichtingLichtbron.waarde

    @punctueleVerlichtingLichtbron.setter
    def punctueleVerlichtingLichtbron(self, value):
        self._punctueleVerlichtingLichtbron.set_waarde(value, owner=self)

    @property
    def verlichtingToestelMerkEnType(self):
        """punctuele verlichting toestel merk en type"""
        return self._verlichtingToestelMerkEnType.waarde

    @verlichtingToestelMerkEnType.setter
    def verlichtingToestelMerkEnType(self, value):
        self._verlichtingToestelMerkEnType.set_waarde(value, owner=self)

    @property
    def redenLichtmastBuitenGebruik(self):
        """afhankelijke eigenschap die enkel moet getoond worden indien waarde "buiten gebruik" ja. keuzelijst (niet van toepassing, normale slijtage, averij, andere)"""
        return self._redenLichtmastBuitenGebruik.waarde

    @redenLichtmastBuitenGebruik.setter
    def redenLichtmastBuitenGebruik(self, value):
        self._redenLichtmastBuitenGebruik.set_waarde(value, owner=self)

    @property
    def risicovollePaal(self):
        """ja als paal extra aandacht vraagt zie inspectiehandboek voor definitie : te bepalen door projectingenieur/toezichter dus niet wijzigbaar voor aannemer"""
        return self._risicovollePaal.waarde

    @risicovollePaal.setter
    def risicovollePaal(self, value):
        self._risicovollePaal.set_waarde(value, owner=self)

    @property
    def toestandBouten(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandBouten.waarde

    @toestandBouten.setter
    def toestandBouten(self, value):
        self._toestandBouten.set_waarde(value, owner=self)

    @property
    def toestandDeurtje(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandDeurtje.waarde

    @toestandDeurtje.setter
    def toestandDeurtje(self, value):
        self._toestandDeurtje.set_waarde(value, owner=self)

    @property
    def toestandFundering(self):
        """Definitie nog toe te voegen voor eigenschap toestand fundering"""
        return self._toestandFundering.waarde

    @toestandFundering.setter
    def toestandFundering(self, value):
        self._toestandFundering.set_waarde(value, owner=self)

    @property
    def toestandPaal(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandPaal.waarde

    @toestandPaal.setter
    def toestandPaal(self, value):
        self._toestandPaal.set_waarde(value, owner=self)

    @property
    def toestandVerlichtingstoestellen(self):
        """keuzelijst (OK, OK met opmerkingen, Ã©Ã©n of meer toestellen of lampen defect, niet gekend)"""
        return self._toestandVerlichtingstoestellen.waarde

    @toestandVerlichtingstoestellen.setter
    def toestandVerlichtingstoestellen(self, value):
        self._toestandVerlichtingstoestellen.set_waarde(value, owner=self)

    @property
    def toestelkleur(self):
        """toestelkleur in RAL"""
        return self._toestelkleur.waarde

    @toestelkleur.setter
    def toestelkleur(self, value):
        self._toestelkleur.set_waarde(value, owner=self)

    @property
    def verlichtingOpstelling(self):
        """Opstelling van de verlichting (zijberm of middenberm)"""
        return self._verlichtingOpstelling.waarde

    @verlichtingOpstelling.setter
    def verlichtingOpstelling(self, value):
        self._verlichtingOpstelling.set_waarde(value, owner=self)

    @property
    def verlichtingsniveauLed(self):
        """Definitie nog toe te voegen voor eigenschap verlichtingsniveau LED"""
        return self._verlichtingsniveauLed.waarde

    @verlichtingsniveauLed.setter
    def verlichtingsniveauLed(self, value):
        self._verlichtingsniveauLed.set_waarde(value, owner=self)

    @property
    def verlichtingstoestelSysteemvermogen(self):
        """vermogen (in Watt) van het verlichtingstoestel"""
        return self._verlichtingstoestelSysteemvermogen.waarde

    @verlichtingstoestelSysteemvermogen.setter
    def verlichtingstoestelSysteemvermogen(self, value):
        self._verlichtingstoestelSysteemvermogen.set_waarde(value, owner=self)

    @property
    def verlichtingstype(self):
        """keuzelijst met types verlichting (doorlopende straatverlichting, rotonde verlichting, punctuele verlichting, projector, tunnelverlichting)"""
        return self._verlichtingstype.waarde

    @verlichtingstype.setter
    def verlichtingstype(self, value):
        self._verlichtingstype.set_waarde(value, owner=self)

    @property
    def vsaSperfilter(self):
        """ja als sperfilter op vsa"""
        return self._vsaSperfilter.waarde

    @vsaSperfilter.setter
    def vsaSperfilter(self, value):
        self._vsaSperfilter.set_waarde(value, owner=self)

