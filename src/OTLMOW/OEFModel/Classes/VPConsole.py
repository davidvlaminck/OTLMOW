# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class VPConsole(EMObject):
    """console wegverlichting"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VPConsole'
    label = 'Console wegverlichting'

    def __init__(self):
        super().__init__()

        self._ledVerlichting = EMAttribuut(field=BooleanField,
                                           naam='LED verlichting',
                                           label='LED verlichting',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ledVerlichting',
                                           definitie='Definitie nog toe te voegen voor eigenschap LED verlichting',
                                           owner=self)

        self._ralKleurVpconsole = EMAttribuut(field=StringField,
                                              naam='RAL kleur (VPCONSOLE)',
                                              label='RAL kleur (VPCONSOLE)',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.ralKleurVpconsole',
                                              definitie='tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden',
                                              owner=self)

        self._vsaType = EMAttribuut(field=StringField,
                                    naam='VSA type',
                                    label='VSA type',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaType',
                                    definitie='keuzelijst elektromagnetisch, elektronisch, niet gekend',
                                    owner=self)

        self._vermoedenSokkelAsbesthoudend = EMAttribuut(field=BooleanField,
                                                         naam='Vermoeden sokkel asbesthoudend',
                                                         label='Vermoeden sokkel asbesthoudend',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.vermoedenSokkelAsbesthoudend',
                                                         definitie='(Vermoeden) sokkel asbesthoudend',
                                                         owner=self)

        self._aanstuurstroomDriversInMa = EMAttribuut(field=StringField,
                                                      naam='aanstuurstroom drivers (in_mA)',
                                                      label='aanstuurstroom drivers (in_mA)',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aanstuurstroomDriversInMa',
                                                      definitie='Definitie nog toe te voegen voor eigenschap aanstuurstroom drivers (in_mA)',
                                                      owner=self)

        self._aantalVsaVervangen = EMAttribuut(field=FloatOrDecimalField,
                                               naam='aantal VSA vervangen',
                                               label='aantal VSA vervangen',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalVsaVervangen',
                                               definitie='Definitie nog toe te voegen voor eigenschap aantal VSA vervangen',
                                               owner=self)

        self._aantalDriversPerToestel = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='aantal drivers per toestel',
                                                    label='aantal drivers per toestel',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalDriversPerToestel',
                                                    definitie='Definitie nog toe te voegen voor eigenschap aantal drivers per toestel',
                                                    owner=self)

        self._aantalKlemmenblokkenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                          naam='aantal klemmenblokken vervangen',
                                                          label='aantal klemmenblokken vervangen',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalKlemmenblokkenVervangen',
                                                          definitie='Definitie nog toe te voegen voor eigenschap aantal klemmenblokken vervangen',
                                                          owner=self)

        self._aantalLampenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                  naam='aantal lampen vervangen',
                                                  label='aantal lampen vervangen',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalLampenVervangen',
                                                  definitie='Definitie nog toe te voegen voor eigenschap aantal lampen vervangen',
                                                  owner=self)

        self._aantalLamphoudersVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                       naam='aantal lamphouders vervangen',
                                                       label='aantal lamphouders vervangen',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalLamphoudersVervangen',
                                                       definitie='Definitie nog toe te voegen voor eigenschap aantal lamphouders vervangen',
                                                       owner=self)

        self._aantalStartersVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='aantal starters vervangen',
                                                    label='aantal starters vervangen',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalStartersVervangen',
                                                    definitie='Definitie nog toe te voegen voor eigenschap aantal starters vervangen',
                                                    owner=self)

        self._aantalTeVerlichtenRijvakkenLed = EMAttribuut(field=StringField,
                                                           naam='aantal te verlichten rijvakken LED',
                                                           label='aantal te verlichten rijvakken LED',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalTeVerlichtenRijvakkenLed',
                                                           definitie='Definitie nog toe te voegen voor eigenschap aantal te verlichten rijvakken LED',
                                                           owner=self)

        self._aantalVerlichtingstoestellen = EMAttribuut(field=FloatOrDecimalField,
                                                         naam='aantal verlichtingstoestellen',
                                                         label='aantal verlichtingstoestellen',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalVerlichtingstoestellen',
                                                         definitie='Definitie nog toe te voegen voor eigenschap aantal verlichtingstoestellen',
                                                         owner=self)

        self._aantalZekeringenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='aantal zekeringen vervangen',
                                                      label='aantal zekeringen vervangen',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalZekeringenVervangen',
                                                      definitie='Definitie nog toe te voegen voor eigenschap aantal zekeringen vervangen',
                                                      owner=self)

        self._andereOnderhoudsacties = EMAttribuut(field=StringField,
                                                   naam='andere onderhoudsacties',
                                                   label='andere onderhoudsacties',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.andereOnderhoudsacties',
                                                   definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                   owner=self)

        self._armatuurkleur = EMAttribuut(field=StringField,
                                          naam='armatuurkleur',
                                          label='armatuurkleur',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.armatuurkleur',
                                          definitie='armatuurkleur voor legacy verlichting',
                                          owner=self)

        self._brandurenLed = EMAttribuut(field=FloatOrDecimalField,
                                         naam='branduren LED',
                                         label='branduren LED',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.brandurenLed',
                                         definitie='Definitie nog toe te voegen voor eigenschap branduren LED',
                                         owner=self)

        self._consoleBuitenGebruik = EMAttribuut(field=BooleanField,
                                                 naam='console buiten gebruik',
                                                 label='console buiten gebruik',
                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.consoleBuitenGebruik',
                                                 definitie='indien console nutteloos is (geen lichtpunt meer), kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering',
                                                 owner=self)

        self._contractnummerLeveringLed = EMAttribuut(field=StringField,
                                                      naam='contractnummer levering LED',
                                                      label='contractnummer levering LED',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.contractnummerLeveringLed',
                                                      definitie='Definitie nog toe te voegen voor eigenschap contractnummer levering LED',
                                                      owner=self)

        self._datumConsoleGeschilderd = EMAttribuut(field=DateField,
                                                    naam='datum console geschilderd',
                                                    label='datum console geschilderd',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.datumConsoleGeschilderd',
                                                    definitie='datum waarop console laatste keer is geschilderd',
                                                    owner=self)

        self._datumConsoleVernieuwd = EMAttribuut(field=DateField,
                                                  naam='datum console vernieuwd',
                                                  label='datum console vernieuwd',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.datumConsoleVernieuwd',
                                                  definitie='datum waarop de console geplaatst is',
                                                  owner=self)

        self._datumInstallatieLed = EMAttribuut(field=DateField,
                                                naam='datum installatie LED',
                                                label='datum installatie LED',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumInstallatieLed',
                                                definitie='Definitie nog toe te voegen voor eigenschap datum installatie LED',
                                                owner=self)

        self._directGevaar = EMAttribuut(field=BooleanField,
                                         naam='direct gevaar',
                                         label='direct gevaar',
                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.directGevaar',
                                         definitie='Definitie nog toe te voegen voor eigenschap direct gevaar',
                                         owner=self)

        self._externeRoestvorming = EMAttribuut(field=StringField,
                                                naam='externe roestvorming',
                                                label='externe roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.externeRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek',
                                                owner=self)

        self._geschilderd = EMAttribuut(field=BooleanField,
                                        naam='geschilderd',
                                        label='geschilderd',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.geschilderd',
                                        definitie='corrosiebescherming geschilderd of niet ?',
                                        owner=self)

        self._inclinatiehoekLed = EMAttribuut(field=FloatOrDecimalField,
                                              naam='inclinatiehoek LED',
                                              label='inclinatiehoek LED',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.inclinatiehoekLed',
                                              definitie='Definitie nog toe te voegen voor eigenschap inclinatiehoek LED',
                                              owner=self)

        self._kleurtemperatuurLed = EMAttribuut(field=StringField,
                                                naam='kleurtemperatuur LED',
                                                label='kleurtemperatuur LED',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.kleurtemperatuurLed',
                                                definitie='Definitie nog toe te voegen voor eigenschap kleurtemperatuur LED',
                                                owner=self)

        self._lampType = EMAttribuut(field=StringField,
                                     naam='lamp type',
                                     label='lamp type',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lampType',
                                     definitie='Lijst lamptypes',
                                     owner=self)

        self._lichtpunthoogteTovRijweg = EMAttribuut(field=FloatOrDecimalField,
                                                     naam='lichtpunthoogte tov rijweg',
                                                     label='lichtpunthoogte tov rijweg',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lichtpunthoogteTovRijweg',
                                                     definitie='Definitie nog toe te voegen voor eigenschap lichtpunthoogte tov rijweg',
                                                     owner=self)

        self._lumenPakketLed = EMAttribuut(field=FloatOrDecimalField,
                                           naam='lumen pakket LED',
                                           label='lumen pakket LED',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.lumenPakketLed',
                                           definitie='Definitie nog toe te voegen voor eigenschap lumen pakket LED',
                                           owner=self)

        self._merkEnTypeLed = EMAttribuut(field=StringField,
                                          naam='merk en type LED',
                                          label='merk en type LED',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.merkEnTypeLed',
                                          definitie='Definitie nog toe te voegen voor eigenschap merk en type LED',
                                          owner=self)

        self._nummerLeesbaar = EMAttribuut(field=StringField,
                                           naam='nummer leesbaar',
                                           label='nummer leesbaar',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.nummerLeesbaar',
                                           definitie='keuzelijst en schaalverdeling volgens inspectiehandboek',
                                           owner=self)

        self._nummerVoedingskringVpconsole = EMAttribuut(field=StringField,
                                                         naam='nummer voedingskring (VPCONSOLE)',
                                                         label='nummer voedingskring (VPCONSOLE)',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.nummerVoedingskringVpconsole',
                                                         definitie='identificatie voedingskring : tekstveld om variatie provincies op te vangen : kring A, B, C, ... of kring 1, 2, 9, ... of ...',
                                                         owner=self)

        self._opmerkingInventarisConsole = EMAttribuut(field=StringField,
                                                       naam='opmerking inventaris console',
                                                       label='opmerking inventaris console',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.opmerkingInventarisConsole',
                                                       definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                       owner=self)

        self._opmerkingInventarisVerlichtingstoestel = EMAttribuut(field=StringField,
                                                                   naam='opmerking inventaris verlichtingstoestel',
                                                                   label='opmerking inventaris verlichtingstoestel',
                                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingInventarisVerlichtingstoestel',
                                                                   definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                                   owner=self)

        self._opmerkingToestandConsole = EMAttribuut(field=StringField,
                                                     naam='opmerking toestand console',
                                                     label='opmerking toestand console',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPConsole.opmerkingToestandConsole',
                                                     definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                     owner=self)

        self._opmerkingToestandVerlichtingstoestel = EMAttribuut(field=StringField,
                                                                 naam='opmerking toestand verlichtingstoestel',
                                                                 label='opmerking toestand verlichtingstoestel',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingToestandVerlichtingstoestel',
                                                                 definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden',
                                                                 owner=self)

        self._optiekLed = EMAttribuut(field=StringField,
                                      naam='optiek LED',
                                      label='optiek LED',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPLMast.optiekLed',
                                      definitie='optiek LED',
                                      owner=self)

        self._overhangLed = EMAttribuut(field=StringField,
                                        naam='overhang LED',
                                        label='overhang LED',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.overhangLed',
                                        definitie='Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan',
                                        owner=self)

        self._redenConsoleBuitenGebruik = EMAttribuut(field=StringField,
                                                      naam='reden console buiten gebruik',
                                                      label='reden console buiten gebruik',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VPConsole.redenConsoleBuitenGebruik',
                                                      definitie='afhankelijke eigenschap die enkel moet getoond worden indien waarde "buiten gebruik" ja. keuzelijst (niet van toepassing, normale slijtage, averij, andere)',
                                                      owner=self)

        self._serienummerLed = EMAttribuut(field=StringField,
                                           naam='serienummer LED',
                                           label='serienummer LED',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.serienummerLed',
                                           definitie='Definitie nog toe te voegen voor eigenschap serienummer LED',
                                           owner=self)

        self._serienummerArmatuurcontroller = EMAttribuut(field=StringField,
                                                          naam='serienummer armatuurcontroller',
                                                          label='serienummer armatuurcontroller',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.serienummerArmatuurcontroller',
                                                          definitie='Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller',
                                                          owner=self)

        self._toestandConsole = EMAttribuut(field=StringField,
                                            naam='toestand console',
                                            label='toestand console',
                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#VPConsole.toestandConsole',
                                            definitie='keuzelijst en schaalverdeling volgens inspectiehandboek',
                                            owner=self)

        self._toestandVerankering = EMAttribuut(field=StringField,
                                                naam='toestand verankering',
                                                label='toestand verankering',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.toestandVerankering',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek',
                                                owner=self)

        self._toestandVerlichtingstoestellen = EMAttribuut(field=StringField,
                                                           naam='toestand verlichtingstoestellen',
                                                           label='toestand verlichtingstoestellen',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.toestandVerlichtingstoestellen',
                                                           definitie='keuzelijst (OK, OK met opmerkingen, Ã©Ã©n of meer toestellen of lampen defect, niet gekend)',
                                                           owner=self)

        self._verlichtingsniveauLed = EMAttribuut(field=StringField,
                                                  naam='verlichtingsniveau LED',
                                                  label='verlichtingsniveau LED',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingsniveauLed',
                                                  definitie='Definitie nog toe te voegen voor eigenschap verlichtingsniveau LED',
                                                  owner=self)

        self._verlichtingstoestelMerkEnType = EMAttribuut(field=StringField,
                                                          naam='verlichtingstoestel merk en type',
                                                          label='verlichtingstoestel merk en type',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstoestelMerkEnType',
                                                          definitie='Lijst verlichtingstoestellen',
                                                          owner=self)

        self._verlichtingstoestelSysteemvermogen = EMAttribuut(field=FloatOrDecimalField,
                                                               naam='verlichtingstoestel systeemvermogen',
                                                               label='verlichtingstoestel systeemvermogen',
                                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstoestelSysteemvermogen',
                                                               definitie='vermogen (in Watt) van het verlichtingstoestel',
                                                               owner=self)

        self._verlichtingstype = EMAttribuut(field=StringField,
                                             naam='verlichtingstype',
                                             label='verlichtingstype',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingstype',
                                             definitie='keuzelijst met types verlichting (doorlopende straatverlichting, rotonde verlichting, punctuele verlichting, projector, tunnelverlichting)',
                                             owner=self)

        self._vsaSperfilter = EMAttribuut(field=BooleanField,
                                          naam='vsa sperfilter',
                                          label='vsa sperfilter',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vsaSperfilter',
                                          definitie='ja als sperfilter op vsa',
                                          owner=self)

    @property
    def ledVerlichting(self):
        """Definitie nog toe te voegen voor eigenschap LED verlichting"""
        return self._ledVerlichting.waarde

    @ledVerlichting.setter
    def ledVerlichting(self, value):
        self._ledVerlichting.set_waarde(value, owner=self)

    @property
    def ralKleurVpconsole(self):
        """tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden"""
        return self._ralKleurVpconsole.waarde

    @ralKleurVpconsole.setter
    def ralKleurVpconsole(self, value):
        self._ralKleurVpconsole.set_waarde(value, owner=self)

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
    def brandurenLed(self):
        """Definitie nog toe te voegen voor eigenschap branduren LED"""
        return self._brandurenLed.waarde

    @brandurenLed.setter
    def brandurenLed(self, value):
        self._brandurenLed.set_waarde(value, owner=self)

    @property
    def consoleBuitenGebruik(self):
        """indien console nutteloos is (geen lichtpunt meer), kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering"""
        return self._consoleBuitenGebruik.waarde

    @consoleBuitenGebruik.setter
    def consoleBuitenGebruik(self, value):
        self._consoleBuitenGebruik.set_waarde(value, owner=self)

    @property
    def contractnummerLeveringLed(self):
        """Definitie nog toe te voegen voor eigenschap contractnummer levering LED"""
        return self._contractnummerLeveringLed.waarde

    @contractnummerLeveringLed.setter
    def contractnummerLeveringLed(self, value):
        self._contractnummerLeveringLed.set_waarde(value, owner=self)

    @property
    def datumConsoleGeschilderd(self):
        """datum waarop console laatste keer is geschilderd"""
        return self._datumConsoleGeschilderd.waarde

    @datumConsoleGeschilderd.setter
    def datumConsoleGeschilderd(self, value):
        self._datumConsoleGeschilderd.set_waarde(value, owner=self)

    @property
    def datumConsoleVernieuwd(self):
        """datum waarop de console geplaatst is"""
        return self._datumConsoleVernieuwd.waarde

    @datumConsoleVernieuwd.setter
    def datumConsoleVernieuwd(self, value):
        self._datumConsoleVernieuwd.set_waarde(value, owner=self)

    @property
    def datumInstallatieLed(self):
        """Definitie nog toe te voegen voor eigenschap datum installatie LED"""
        return self._datumInstallatieLed.waarde

    @datumInstallatieLed.setter
    def datumInstallatieLed(self, value):
        self._datumInstallatieLed.set_waarde(value, owner=self)

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
    def nummerLeesbaar(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._nummerLeesbaar.waarde

    @nummerLeesbaar.setter
    def nummerLeesbaar(self, value):
        self._nummerLeesbaar.set_waarde(value, owner=self)

    @property
    def nummerVoedingskringVpconsole(self):
        """identificatie voedingskring : tekstveld om variatie provincies op te vangen : kring A, B, C, ... of kring 1, 2, 9, ... of ..."""
        return self._nummerVoedingskringVpconsole.waarde

    @nummerVoedingskringVpconsole.setter
    def nummerVoedingskringVpconsole(self, value):
        self._nummerVoedingskringVpconsole.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisConsole(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisConsole.waarde

    @opmerkingInventarisConsole.setter
    def opmerkingInventarisConsole(self, value):
        self._opmerkingInventarisConsole.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisVerlichtingstoestel(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisVerlichtingstoestel.waarde

    @opmerkingInventarisVerlichtingstoestel.setter
    def opmerkingInventarisVerlichtingstoestel(self, value):
        self._opmerkingInventarisVerlichtingstoestel.set_waarde(value, owner=self)

    @property
    def opmerkingToestandConsole(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingToestandConsole.waarde

    @opmerkingToestandConsole.setter
    def opmerkingToestandConsole(self, value):
        self._opmerkingToestandConsole.set_waarde(value, owner=self)

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
    def redenConsoleBuitenGebruik(self):
        """afhankelijke eigenschap die enkel moet getoond worden indien waarde "buiten gebruik" ja. keuzelijst (niet van toepassing, normale slijtage, averij, andere)"""
        return self._redenConsoleBuitenGebruik.waarde

    @redenConsoleBuitenGebruik.setter
    def redenConsoleBuitenGebruik(self, value):
        self._redenConsoleBuitenGebruik.set_waarde(value, owner=self)

    @property
    def serienummerLed(self):
        """Definitie nog toe te voegen voor eigenschap serienummer LED"""
        return self._serienummerLed.waarde

    @serienummerLed.setter
    def serienummerLed(self, value):
        self._serienummerLed.set_waarde(value, owner=self)

    @property
    def serienummerArmatuurcontroller(self):
        """Definitie nog toe te voegen voor eigenschap serienummer armatuurcontroller"""
        return self._serienummerArmatuurcontroller.waarde

    @serienummerArmatuurcontroller.setter
    def serienummerArmatuurcontroller(self, value):
        self._serienummerArmatuurcontroller.set_waarde(value, owner=self)

    @property
    def toestandConsole(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandConsole.waarde

    @toestandConsole.setter
    def toestandConsole(self, value):
        self._toestandConsole.set_waarde(value, owner=self)

    @property
    def toestandVerankering(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandVerankering.waarde

    @toestandVerankering.setter
    def toestandVerankering(self, value):
        self._toestandVerankering.set_waarde(value, owner=self)

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

