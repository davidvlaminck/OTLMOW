# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class VPLMast(EMObject):
    """lichtmast wegverlichting"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast'
    label = 'Lichtmast wegverlichting'

    def __init__(self):
        super().__init__()

        self._ledVerlichting = EMAttribuut(field=BooleanField,
                                           naam='LED verlichting',
                                           label='LED verlichting',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ledVerlichting',
                                           definitie='Definitie nog toe te voegen voor eigenschap LED verlichting')

        self._ralKleurVplmast = EMAttribuut(field=StringField,
                                            naam='RAL kleur (VPLMAST)',
                                            label='RAL kleur (VPLMAST)',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.ralKleurVplmast',
                                            definitie='tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden')

        self._vsaType = EMAttribuut(field=StringField,
                                    naam='VSA type',
                                    label='VSA type',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaType',
                                    definitie='keuzelijst elektromagnetisch, elektronisch, niet gekend')

        self._vermoedenSokkelAsbesthoudend = EMAttribuut(field=BooleanField,
                                                         naam='Vermoeden sokkel asbesthoudend',
                                                         label='Vermoeden sokkel asbesthoudend',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.vermoedenSokkelAsbesthoudend',
                                                         definitie='(Vermoeden) sokkel asbesthoudend')

        self._aanstuurstroomDriversInMa = EMAttribuut(field=StringField,
                                                      naam='aanstuurstroom drivers (in_mA)',
                                                      label='aanstuurstroom drivers (in_mA)',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aanstuurstroomDriversInMa',
                                                      definitie='Definitie nog toe te voegen voor eigenschap aanstuurstroom drivers (in_mA)')

        self._aantalVsaVervangen = EMAttribuut(field=FloatOrDecimalField,
                                               naam='aantal VSA vervangen',
                                               label='aantal VSA vervangen',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalVsaVervangen',
                                               definitie='Definitie nog toe te voegen voor eigenschap aantal VSA vervangen')

        self._aantalArmen = EMAttribuut(field=StringField,
                                        naam='aantal armen',
                                        label='aantal armen',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.aantalArmen',
                                        definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast \'M\', \'MS\', \'B\',\'BS\', \'K\' of \'KS\' dan 0,1, 2,3 of 4. Anders altijd 0.")

        self._aantalDriversPerToestel = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='aantal drivers per toestel',
                                                    label='aantal drivers per toestel',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalDriversPerToestel',
                                                    definitie='Definitie nog toe te voegen voor eigenschap aantal drivers per toestel')

        self._aantalKlemmenblokkenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                          naam='aantal klemmenblokken vervangen',
                                                          label='aantal klemmenblokken vervangen',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalKlemmenblokkenVervangen',
                                                          definitie='Definitie nog toe te voegen voor eigenschap aantal klemmenblokken vervangen')

        self._aantalLampenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                  naam='aantal lampen vervangen',
                                                  label='aantal lampen vervangen',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalLampenVervangen',
                                                  definitie='Definitie nog toe te voegen voor eigenschap aantal lampen vervangen')

        self._aantalLamphoudersVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                       naam='aantal lamphouders vervangen',
                                                       label='aantal lamphouders vervangen',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalLamphoudersVervangen',
                                                       definitie='Definitie nog toe te voegen voor eigenschap aantal lamphouders vervangen')

        self._aantalStartersVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='aantal starters vervangen',
                                                    label='aantal starters vervangen',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalStartersVervangen',
                                                    definitie='Definitie nog toe te voegen voor eigenschap aantal starters vervangen')

        self._aantalTeVerlichtenRijvakkenLed = EMAttribuut(field=StringField,
                                                           naam='aantal te verlichten rijvakken LED',
                                                           label='aantal te verlichten rijvakken LED',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalTeVerlichtenRijvakkenLed',
                                                           definitie='Definitie nog toe te voegen voor eigenschap aantal te verlichten rijvakken LED')

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

        self._andereOnderhoudsacties = EMAttribuut(field=StringField,
                                                   naam='andere onderhoudsacties',
                                                   label='andere onderhoudsacties',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.andereOnderhoudsacties',
                                                   definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._armatuurkleur = EMAttribuut(field=StringField,
                                          naam='armatuurkleur',
                                          label='armatuurkleur',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.armatuurkleur',
                                          definitie='armatuurkleur voor legacy verlichting')

        self._armlengte = EMAttribuut(field=StringField,
                                      naam='armlengte',
                                      label='armlengte',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.armlengte',
                                      kardinaliteit='1..2',
                                      definitie="keuzelijst met een vijftal veel gebruikte waarden en keuzes \'niet van toepassing\' en  \'andere\'")

        self._bevestigingswijzeMeerdereToestellen = EMAttribuut(field=StringField,
                                                                naam='bevestigingswijze meerdere toestellen',
                                                                label='bevestigingswijze meerdere toestellen',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.bevestigingswijzeMeerdereToestellen',
                                                                definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere).')

        self._brandurenLed = EMAttribuut(field=FloatOrDecimalField,
                                         naam='branduren LED',
                                         label='branduren LED',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.brandurenLed',
                                         definitie='Definitie nog toe te voegen voor eigenschap branduren LED')

        self._contractnummerLeveringLed = EMAttribuut(field=StringField,
                                                      naam='contractnummer levering LED',
                                                      label='contractnummer levering LED',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.contractnummerLeveringLed',
                                                      definitie='Definitie nog toe te voegen voor eigenschap contractnummer levering LED')

        self._datumInstallatieLed = EMAttribuut(field=DateField,
                                                naam='datum installatie LED',
                                                label='datum installatie LED',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumInstallatieLed',
                                                definitie='Definitie nog toe te voegen voor eigenschap datum installatie LED')

        self._datumLichtmastGeschilderd = EMAttribuut(field=DateField,
                                                      naam='datum lichtmast geschilderd',
                                                      label='datum lichtmast geschilderd',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.datumLichtmastGeschilderd',
                                                      definitie='datum waarop lichtmast laatste keer is geschilderd')

        self._datumLichtmastVernieuwd = EMAttribuut(field=DateField,
                                                    naam='datum lichtmast vernieuwd',
                                                    label='datum lichtmast vernieuwd',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.datumLichtmastVernieuwd',
                                                    definitie='datum waarop de lichtmast geplaatst is')

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

        self._geschilderd = EMAttribuut(field=BooleanField,
                                        naam='geschilderd',
                                        label='geschilderd',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.geschilderd',
                                        definitie='corrosiebescherming geschilderd of niet ?')

        self._inclinatiehoekLed = EMAttribuut(field=FloatOrDecimalField,
                                              naam='inclinatiehoek LED',
                                              label='inclinatiehoek LED',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.inclinatiehoekLed',
                                              definitie='Definitie nog toe te voegen voor eigenschap inclinatiehoek LED')

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

        self._lampType = EMAttribuut(field=StringField,
                                     naam='lamp type',
                                     label='lamp type',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lampType',
                                     definitie='Lijst lamptypes')

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

        self._lichtmastType = EMAttribuut(field=StringField,
                                          naam='lichtmast type',
                                          label='lichtmast type',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.lichtmastType',
                                          definitie='Lijst lichtmasttypes')

        self._lichtpunthoogteTovRijweg = EMAttribuut(field=FloatOrDecimalField,
                                                     naam='lichtpunthoogte tov rijweg',
                                                     label='lichtpunthoogte tov rijweg',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lichtpunthoogteTovRijweg',
                                                     definitie='Definitie nog toe te voegen voor eigenschap lichtpunthoogte tov rijweg')

        self._lumenPakketLed = EMAttribuut(field=FloatOrDecimalField,
                                           naam='lumen pakket LED',
                                           label='lumen pakket LED',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lumenPakketLed',
                                           definitie='Definitie nog toe te voegen voor eigenschap lumen pakket LED')

        self._merkEnTypeLed = EMAttribuut(field=StringField,
                                          naam='merk en type LED',
                                          label='merk en type LED',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.merkEnTypeLed',
                                          definitie='Definitie nog toe te voegen voor eigenschap merk en type LED')

        self._merkEnTypeArmatuurcontroller1 = EMAttribuut(field=StringField,
                                                          naam='merk en type armatuurcontroller 1',
                                                          label='merk en type armatuurcontroller 1',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.merkEnTypeArmatuurcontroller1',
                                                          definitie='Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 1')

        self._merkEnTypeArmatuurcontroller2 = EMAttribuut(field=StringField,
                                                          naam='merk en type armatuurcontroller 2',
                                                          label='merk en type armatuurcontroller 2',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.merkEnTypeArmatuurcontroller2',
                                                          definitie='Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 2')

        self._merkEnTypeArmatuurcontroller3 = EMAttribuut(field=StringField,
                                                          naam='merk en type armatuurcontroller 3',
                                                          label='merk en type armatuurcontroller 3',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.merkEnTypeArmatuurcontroller3',
                                                          definitie='Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 3')

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

        self._opmerkingInventarisPaal = EMAttribuut(field=StringField,
                                                    naam='opmerking inventaris paal',
                                                    label='opmerking inventaris paal',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.opmerkingInventarisPaal',
                                                    definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._opmerkingInventarisVerlichtingstoestel = EMAttribuut(field=StringField,
                                                                   naam='opmerking inventaris verlichtingstoestel',
                                                                   label='opmerking inventaris verlichtingstoestel',
                                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingInventarisVerlichtingstoestel',
                                                                   definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._opmerkingToestandPaal = EMAttribuut(field=StringField,
                                                  naam='opmerking toestand paal',
                                                  label='opmerking toestand paal',
                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPLMast.opmerkingToestandPaal',
                                                  definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._opmerkingToestandVerlichtingstoestel = EMAttribuut(field=StringField,
                                                                 naam='opmerking toestand verlichtingstoestel',
                                                                 label='opmerking toestand verlichtingstoestel',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingToestandVerlichtingstoestel',
                                                                 definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._optiekLed = EMAttribuut(field=StringField,
                                      naam='optiek LED',
                                      label='optiek LED',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.optiekLed',
                                      definitie='optiek LED')

        self._overhangLed = EMAttribuut(field=StringField,
                                        naam='overhang LED',
                                        label='overhang LED',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.overhangLed',
                                        definitie='Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan')

        self._paalhoogte = EMAttribuut(field=StringField,
                                       naam='paalhoogte',
                                       label='paalhoogte',
                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.paalhoogte',
                                       definitie='Lijst paalhoogtes')

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

        self._serienummerLed1 = EMAttribuut(field=StringField,
                                            naam='serienummer LED 1',
                                            label='serienummer LED 1',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerLed1',
                                            definitie='Definitie nog toe te voegen voor eigenschap serienummer LED 1')

        self._serienummerLed2 = EMAttribuut(field=StringField,
                                            naam='serienummer LED 2',
                                            label='serienummer LED 2',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerLed2',
                                            definitie='Definitie nog toe te voegen voor eigenschap serienummer LED 2')

        self._serienummerLed3 = EMAttribuut(field=StringField,
                                            naam='serienummer LED 3',
                                            label='serienummer LED 3',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerLed3',
                                            definitie='Definitie nog toe te voegen voor eigenschap serienummer LED 3')

        self._serienummerArmatuurcontroller1 = EMAttribuut(field=StringField,
                                                           naam='serienummer armatuurcontroller 1',
                                                           label='serienummer armatuurcontroller 1',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerArmatuurcontroller1',
                                                           definitie='Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 1')

        self._serienummerArmatuurcontroller2 = EMAttribuut(field=StringField,
                                                           naam='serienummer armatuurcontroller 2',
                                                           label='serienummer armatuurcontroller 2',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerArmatuurcontroller2',
                                                           definitie='Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 2')

        self._serienummerArmatuurcontroller3 = EMAttribuut(field=StringField,
                                                           naam='serienummer armatuurcontroller 3',
                                                           label='serienummer armatuurcontroller 3',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.serienummerArmatuurcontroller3',
                                                           definitie='Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 3')

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

        self._toestandFunderingVplmast = EMAttribuut(field=StringField,
                                                     naam='toestand fundering (VPLMAST)',
                                                     label='toestand fundering (VPLMAST)',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPLMast.toestandFunderingVplmast',
                                                     definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

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

        self._verlichtingsniveauLed = EMAttribuut(field=StringField,
                                                  naam='verlichtingsniveau LED',
                                                  label='verlichtingsniveau LED',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingsniveauLed',
                                                  definitie='Definitie nog toe te voegen voor eigenschap verlichtingsniveau LED')

        self._verlichtingstoestelMerkEnType = EMAttribuut(field=StringField,
                                                          naam='verlichtingstoestel merk en type',
                                                          label='verlichtingstoestel merk en type',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstoestelMerkEnType',
                                                          definitie='Lijst verlichtingstoestellen')

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
    def ralKleurVplmast(self):
        """tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden"""
        return self._ralKleurVplmast.waarde

    @ralKleurVplmast.setter
    def ralKleurVplmast(self, value):
        self._ralKleurVplmast.set_waarde(value, owner=self)

    @property
    def vsaType(self):
        """keuzelijst elektromagnetisch, elektronisch, niet gekend"""
        return self._vsaType.waarde

    @vsaType.setter
    def vsaType(self, value):
        self._vsaType.set_waarde(value, owner=self)

    @property
    def vermoedenSokkelAsbesthoudend(self):
        """(Vermoeden) sokkel asbesthoudend"""
        return self._vermoedenSokkelAsbesthoudend.waarde

    @vermoedenSokkelAsbesthoudend.setter
    def vermoedenSokkelAsbesthoudend(self, value):
        self._vermoedenSokkelAsbesthoudend.set_waarde(value, owner=self)

    @property
    def aanstuurstroomDriversInMa(self):
        """Definitie nog toe te voegen voor eigenschap aanstuurstroom drivers (in_mA)"""
        return self._aanstuurstroomDriversInMa.waarde

    @aanstuurstroomDriversInMa.setter
    def aanstuurstroomDriversInMa(self, value):
        self._aanstuurstroomDriversInMa.set_waarde(value, owner=self)

    @property
    def aantalVsaVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal VSA vervangen"""
        return self._aantalVsaVervangen.waarde

    @aantalVsaVervangen.setter
    def aantalVsaVervangen(self, value):
        self._aantalVsaVervangen.set_waarde(value, owner=self)

    @property
    def aantalArmen(self):
        """keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast \'M\', \'MS\', \'B\',\'BS\', \'K\' of \'KS\' dan 0,1, 2,3 of 4. Anders altijd 0."""
        return self._aantalArmen.waarde

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def aantalDriversPerToestel(self):
        """Definitie nog toe te voegen voor eigenschap aantal drivers per toestel"""
        return self._aantalDriversPerToestel.waarde

    @aantalDriversPerToestel.setter
    def aantalDriversPerToestel(self, value):
        self._aantalDriversPerToestel.set_waarde(value, owner=self)

    @property
    def aantalKlemmenblokkenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal klemmenblokken vervangen"""
        return self._aantalKlemmenblokkenVervangen.waarde

    @aantalKlemmenblokkenVervangen.setter
    def aantalKlemmenblokkenVervangen(self, value):
        self._aantalKlemmenblokkenVervangen.set_waarde(value, owner=self)

    @property
    def aantalLampenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal lampen vervangen"""
        return self._aantalLampenVervangen.waarde

    @aantalLampenVervangen.setter
    def aantalLampenVervangen(self, value):
        self._aantalLampenVervangen.set_waarde(value, owner=self)

    @property
    def aantalLamphoudersVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal lamphouders vervangen"""
        return self._aantalLamphoudersVervangen.waarde

    @aantalLamphoudersVervangen.setter
    def aantalLamphoudersVervangen(self, value):
        self._aantalLamphoudersVervangen.set_waarde(value, owner=self)

    @property
    def aantalStartersVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal starters vervangen"""
        return self._aantalStartersVervangen.waarde

    @aantalStartersVervangen.setter
    def aantalStartersVervangen(self, value):
        self._aantalStartersVervangen.set_waarde(value, owner=self)

    @property
    def aantalTeVerlichtenRijvakkenLed(self):
        """Definitie nog toe te voegen voor eigenschap aantal te verlichten rijvakken LED"""
        return self._aantalTeVerlichtenRijvakkenLed.waarde

    @aantalTeVerlichtenRijvakkenLed.setter
    def aantalTeVerlichtenRijvakkenLed(self, value):
        self._aantalTeVerlichtenRijvakkenLed.set_waarde(value, owner=self)

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
    def andereOnderhoudsacties(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._andereOnderhoudsacties.waarde

    @andereOnderhoudsacties.setter
    def andereOnderhoudsacties(self, value):
        self._andereOnderhoudsacties.set_waarde(value, owner=self)

    @property
    def armatuurkleur(self):
        """armatuurkleur voor legacy verlichting"""
        return self._armatuurkleur.waarde

    @armatuurkleur.setter
    def armatuurkleur(self, value):
        self._armatuurkleur.set_waarde(value, owner=self)

    @property
    def armlengte(self):
        """keuzelijst met een vijftal veel gebruikte waarden en keuzes \'niet van toepassing\' en  \'andere\'"""
        return self._armlengte.waarde

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def bevestigingswijzeMeerdereToestellen(self):
        """keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)."""
        return self._bevestigingswijzeMeerdereToestellen.waarde

    @bevestigingswijzeMeerdereToestellen.setter
    def bevestigingswijzeMeerdereToestellen(self, value):
        self._bevestigingswijzeMeerdereToestellen.set_waarde(value, owner=self)

    @property
    def brandurenLed(self):
        """Definitie nog toe te voegen voor eigenschap branduren LED"""
        return self._brandurenLed.waarde

    @brandurenLed.setter
    def brandurenLed(self, value):
        self._brandurenLed.set_waarde(value, owner=self)

    @property
    def contractnummerLeveringLed(self):
        """Definitie nog toe te voegen voor eigenschap contractnummer levering LED"""
        return self._contractnummerLeveringLed.waarde

    @contractnummerLeveringLed.setter
    def contractnummerLeveringLed(self, value):
        self._contractnummerLeveringLed.set_waarde(value, owner=self)

    @property
    def datumInstallatieLed(self):
        """Definitie nog toe te voegen voor eigenschap datum installatie LED"""
        return self._datumInstallatieLed.waarde

    @datumInstallatieLed.setter
    def datumInstallatieLed(self, value):
        self._datumInstallatieLed.set_waarde(value, owner=self)

    @property
    def datumLichtmastGeschilderd(self):
        """datum waarop lichtmast laatste keer is geschilderd"""
        return self._datumLichtmastGeschilderd.waarde

    @datumLichtmastGeschilderd.setter
    def datumLichtmastGeschilderd(self, value):
        self._datumLichtmastGeschilderd.set_waarde(value, owner=self)

    @property
    def datumLichtmastVernieuwd(self):
        """datum waarop de lichtmast geplaatst is"""
        return self._datumLichtmastVernieuwd.waarde

    @datumLichtmastVernieuwd.setter
    def datumLichtmastVernieuwd(self, value):
        self._datumLichtmastVernieuwd.set_waarde(value, owner=self)

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
    def geschilderd(self):
        """corrosiebescherming geschilderd of niet ?"""
        return self._geschilderd.waarde

    @geschilderd.setter
    def geschilderd(self, value):
        self._geschilderd.set_waarde(value, owner=self)

    @property
    def inclinatiehoekLed(self):
        """Definitie nog toe te voegen voor eigenschap inclinatiehoek LED"""
        return self._inclinatiehoekLed.waarde

    @inclinatiehoekLed.setter
    def inclinatiehoekLed(self, value):
        self._inclinatiehoekLed.set_waarde(value, owner=self)

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
    def lampType(self):
        """Lijst lamptypes"""
        return self._lampType.waarde

    @lampType.setter
    def lampType(self, value):
        self._lampType.set_waarde(value, owner=self)

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
    def lichtmastType(self):
        """Lijst lichtmasttypes"""
        return self._lichtmastType.waarde

    @lichtmastType.setter
    def lichtmastType(self, value):
        self._lichtmastType.set_waarde(value, owner=self)

    @property
    def lichtpunthoogteTovRijweg(self):
        """Definitie nog toe te voegen voor eigenschap lichtpunthoogte tov rijweg"""
        return self._lichtpunthoogteTovRijweg.waarde

    @lichtpunthoogteTovRijweg.setter
    def lichtpunthoogteTovRijweg(self, value):
        self._lichtpunthoogteTovRijweg.set_waarde(value, owner=self)

    @property
    def lumenPakketLed(self):
        """Definitie nog toe te voegen voor eigenschap lumen pakket LED"""
        return self._lumenPakketLed.waarde

    @lumenPakketLed.setter
    def lumenPakketLed(self, value):
        self._lumenPakketLed.set_waarde(value, owner=self)

    @property
    def merkEnTypeLed(self):
        """Definitie nog toe te voegen voor eigenschap merk en type LED"""
        return self._merkEnTypeLed.waarde

    @merkEnTypeLed.setter
    def merkEnTypeLed(self, value):
        self._merkEnTypeLed.set_waarde(value, owner=self)

    @property
    def merkEnTypeArmatuurcontroller1(self):
        """Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 1"""
        return self._merkEnTypeArmatuurcontroller1.waarde

    @merkEnTypeArmatuurcontroller1.setter
    def merkEnTypeArmatuurcontroller1(self, value):
        self._merkEnTypeArmatuurcontroller1.set_waarde(value, owner=self)

    @property
    def merkEnTypeArmatuurcontroller2(self):
        """Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 2"""
        return self._merkEnTypeArmatuurcontroller2.waarde

    @merkEnTypeArmatuurcontroller2.setter
    def merkEnTypeArmatuurcontroller2(self, value):
        self._merkEnTypeArmatuurcontroller2.set_waarde(value, owner=self)

    @property
    def merkEnTypeArmatuurcontroller3(self):
        """Definitie nog toe te voegen voor eigenschap merk en type armatuurcontroller 3"""
        return self._merkEnTypeArmatuurcontroller3.waarde

    @merkEnTypeArmatuurcontroller3.setter
    def merkEnTypeArmatuurcontroller3(self, value):
        self._merkEnTypeArmatuurcontroller3.set_waarde(value, owner=self)

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
    def opmerkingInventarisPaal(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisPaal.waarde

    @opmerkingInventarisPaal.setter
    def opmerkingInventarisPaal(self, value):
        self._opmerkingInventarisPaal.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisVerlichtingstoestel(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisVerlichtingstoestel.waarde

    @opmerkingInventarisVerlichtingstoestel.setter
    def opmerkingInventarisVerlichtingstoestel(self, value):
        self._opmerkingInventarisVerlichtingstoestel.set_waarde(value, owner=self)

    @property
    def opmerkingToestandPaal(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingToestandPaal.waarde

    @opmerkingToestandPaal.setter
    def opmerkingToestandPaal(self, value):
        self._opmerkingToestandPaal.set_waarde(value, owner=self)

    @property
    def opmerkingToestandVerlichtingstoestel(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingToestandVerlichtingstoestel.waarde

    @opmerkingToestandVerlichtingstoestel.setter
    def opmerkingToestandVerlichtingstoestel(self, value):
        self._opmerkingToestandVerlichtingstoestel.set_waarde(value, owner=self)

    @property
    def optiekLed(self):
        """optiek LED"""
        return self._optiekLed.waarde

    @optiekLed.setter
    def optiekLed(self, value):
        self._optiekLed.set_waarde(value, owner=self)

    @property
    def overhangLed(self):
        """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan"""
        return self._overhangLed.waarde

    @overhangLed.setter
    def overhangLed(self, value):
        self._overhangLed.set_waarde(value, owner=self)

    @property
    def paalhoogte(self):
        """Lijst paalhoogtes"""
        return self._paalhoogte.waarde

    @paalhoogte.setter
    def paalhoogte(self, value):
        self._paalhoogte.set_waarde(value, owner=self)

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
    def serienummerLed1(self):
        """Definitie nog toe te voegen voor eigenschap serienummer LED 1"""
        return self._serienummerLed1.waarde

    @serienummerLed1.setter
    def serienummerLed1(self, value):
        self._serienummerLed1.set_waarde(value, owner=self)

    @property
    def serienummerLed2(self):
        """Definitie nog toe te voegen voor eigenschap serienummer LED 2"""
        return self._serienummerLed2.waarde

    @serienummerLed2.setter
    def serienummerLed2(self, value):
        self._serienummerLed2.set_waarde(value, owner=self)

    @property
    def serienummerLed3(self):
        """Definitie nog toe te voegen voor eigenschap serienummer LED 3"""
        return self._serienummerLed3.waarde

    @serienummerLed3.setter
    def serienummerLed3(self, value):
        self._serienummerLed3.set_waarde(value, owner=self)

    @property
    def serienummerArmatuurcontroller1(self):
        """Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 1"""
        return self._serienummerArmatuurcontroller1.waarde

    @serienummerArmatuurcontroller1.setter
    def serienummerArmatuurcontroller1(self, value):
        self._serienummerArmatuurcontroller1.set_waarde(value, owner=self)

    @property
    def serienummerArmatuurcontroller2(self):
        """Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 2"""
        return self._serienummerArmatuurcontroller2.waarde

    @serienummerArmatuurcontroller2.setter
    def serienummerArmatuurcontroller2(self, value):
        self._serienummerArmatuurcontroller2.set_waarde(value, owner=self)

    @property
    def serienummerArmatuurcontroller3(self):
        """Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller 3"""
        return self._serienummerArmatuurcontroller3.waarde

    @serienummerArmatuurcontroller3.setter
    def serienummerArmatuurcontroller3(self, value):
        self._serienummerArmatuurcontroller3.set_waarde(value, owner=self)

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
    def toestandFunderingVplmast(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandFunderingVplmast.waarde

    @toestandFunderingVplmast.setter
    def toestandFunderingVplmast(self, value):
        self._toestandFunderingVplmast.set_waarde(value, owner=self)

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
    def verlichtingsniveauLed(self):
        """Definitie nog toe te voegen voor eigenschap verlichtingsniveau LED"""
        return self._verlichtingsniveauLed.waarde

    @verlichtingsniveauLed.setter
    def verlichtingsniveauLed(self, value):
        self._verlichtingsniveauLed.set_waarde(value, owner=self)

    @property
    def verlichtingstoestelMerkEnType(self):
        """Lijst verlichtingstoestellen"""
        return self._verlichtingstoestelMerkEnType.waarde

    @verlichtingstoestelMerkEnType.setter
    def verlichtingstoestelMerkEnType(self, value):
        self._verlichtingstoestelMerkEnType.set_waarde(value, owner=self)

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

