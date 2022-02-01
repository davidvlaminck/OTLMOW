# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SeinbrugIVS(EMObject):
    """Seinbrug met inwendig verlichte signalisatie borden"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SeinbrugIVS'
    label = 'Seinbrug IVSB'

    def __init__(self):
        super().__init__()

        self._ralKleurSeinbrgivs = EMAttribuut(field=StringField,
                                               naam='RAL kleur (SEINBRGIVS)',
                                               label='RAL kleur (SEINBRGIVS)',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.ralKleurSeinbrgivs',
                                               definitie='tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden')

        self._aantalDeurtjesAfschermingenVervangen = EMAttribuut(field=FloatOrDecimalField,
                                                                 naam='aantal deurtjes/afschermingen vervangen',
                                                                 label='aantal deurtjes/afschermingen vervangen',
                                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.aantalDeurtjesAfschermingenVervangen',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap aantal deurtjes/afschermingen vervangen')

        self._aanwezigheidExtraVerhoog = EMAttribuut(field=StringField,
                                                     naam='aanwezigheid extra verhoog',
                                                     label='aanwezigheid extra verhoog',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.aanwezigheidExtraVerhoog',
                                                     definitie='Definitie nog toe te voegen voor eigenschap aanwezigheid extra verhoog')

        self._andereOnderhoudsacties = EMAttribuut(field=StringField,
                                                   naam='andere onderhoudsacties',
                                                   label='andere onderhoudsacties',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.andereOnderhoudsacties',
                                                   definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._datumNieuweSeinbrugIvs = EMAttribuut(field=DateField,
                                                   naam='datum nieuwe seinbrug IVS',
                                                   label='datum nieuwe seinbrug IVS',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.datumNieuweSeinbrugIvs',
                                                   definitie='datum waarop de seinbrug IVS geplaatst is')

        self._datumSeinbrugIvsGeschilderd = EMAttribuut(field=DateField,
                                                        naam='datum seinbrug IVS geschilderd',
                                                        label='datum seinbrug IVS geschilderd',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.datumSeinbrugIvsGeschilderd',
                                                        definitie='datum waarop seinbrug IVS laatste keer is geschilderd')

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

        self._geschilderdSeinbrgivs = EMAttribuut(field=BooleanField,
                                                  naam='geschilderd (SEINBRGIVS)',
                                                  label='geschilderd (SEINBRGIVS)',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.geschilderdSeinbrgivs',
                                                  definitie='corrosiebescherming geschilderd of niet?')

        self._interneRoestvorming = EMAttribuut(field=StringField,
                                                naam='interne roestvorming',
                                                label='interne roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.interneRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._kabelfout = EMAttribuut(field=BooleanField,
                                      naam='kabelfout',
                                      label='kabelfout',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.kabelfout',
                                      definitie='Definitie nog toe te voegen voor eigenschap kabelfout')

        self._ladder = EMAttribuut(field=StringField,
                                   naam='ladder',
                                   label='ladder',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.ladder',
                                   definitie='Definitie nog toe te voegen voor eigenschap ladder')

        self._lengteOverspanningSeinbrgivs = EMAttribuut(field=FloatOrDecimalField,
                                                         naam='lengte overspanning (SEINBRGIVS)',
                                                         label='lengte overspanning (SEINBRGIVS)',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.lengteOverspanningSeinbrgivs',
                                                         definitie='lengte overspanning/uitkraging')

        self._leuningOpDwarsbalk = EMAttribuut(field=StringField,
                                               naam='leuning op dwarsbalk',
                                               label='leuning op dwarsbalk',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.leuningOpDwarsbalk',
                                               definitie='Definitie nog toe te voegen voor eigenschap leuning op dwarsbalk')

        self._minimumVrijeHoogte = EMAttribuut(field=FloatOrDecimalField,
                                               naam='minimum vrije hoogte',
                                               label='minimum vrije hoogte',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.minimumVrijeHoogte',
                                               definitie='Definitie nog toe te voegen voor eigenschap minimum vrije hoogte')

        self._nummerLeesbaar = EMAttribuut(field=StringField,
                                           naam='nummer leesbaar',
                                           label='nummer leesbaar',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.nummerLeesbaar',
                                           definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._opmerkingInventarisSeinbrugIvs = EMAttribuut(field=StringField,
                                                           naam='opmerking inventaris seinbrug IVS',
                                                           label='opmerking inventaris seinbrug IVS',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.opmerkingInventarisSeinbrugIvs',
                                                           definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._opmerkingToestandSeinbrugIvs = EMAttribuut(field=StringField,
                                                         naam='opmerking toestand seinbrug IVS',
                                                         label='opmerking toestand seinbrug IVS',
                                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.opmerkingToestandSeinbrugIvs',
                                                         definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._plaatsBeschadigingSeinbrugIvs = EMAttribuut(field=StringField,
                                                          naam='plaats beschadiging seinbrug IVS',
                                                          label='plaats beschadiging seinbrug IVS',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.plaatsBeschadigingSeinbrugIvs',
                                                          definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden over de plaats van de beschadiging')

        self._plaatsExterneRoestvorming = EMAttribuut(field=StringField,
                                                      naam='plaats externe roestvorming',
                                                      label='plaats externe roestvorming',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.plaatsExterneRoestvorming',
                                                      definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden over de plaats van de externe roestvorming')

        self._redenSeinbrugIvsBuitenGebruik = EMAttribuut(field=StringField,
                                                          naam='reden seinbrug IVS buiten gebruik',
                                                          label='reden seinbrug IVS buiten gebruik',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.redenSeinbrugIvsBuitenGebruik',
                                                          definitie='Definitie nog toe te voegen voor eigenschap reden seinbrug IVS buiten gebruik')

        self._reinigingSteunen = EMAttribuut(field=BooleanField,
                                             naam='reiniging steunen',
                                             label='reiniging steunen',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.reinigingSteunen',
                                             definitie='enkel voor onderhoud IVSB constructies')

        self._seinbrugIvsBuitenGebruik = EMAttribuut(field=BooleanField,
                                                     naam='seinbrug IVS buiten gebruik',
                                                     label='seinbrug IVS buiten gebruik',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.seinbrugIvsBuitenGebruik',
                                                     definitie='indien seinbrug IVS nutteloos is, kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering')

        self._seinbrugTeBehoudenVolgensDienstorder = EMAttribuut(field=BooleanField,
                                                                 naam='seinbrug te behouden volgens dienstorder',
                                                                 label='seinbrug te behouden volgens dienstorder',
                                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.seinbrugTeBehoudenVolgensDienstorder',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap seinbrug te behouden volgens dienstorder')

        self._toestandBoutenKolomDrager = EMAttribuut(field=StringField,
                                                      naam='toestand bouten kolom-drager',
                                                      label='toestand bouten kolom-drager',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandBoutenKolomDrager',
                                                      definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandBoutenKolomVerankering = EMAttribuut(field=StringField,
                                                           naam='toestand bouten kolom-verankering',
                                                           label='toestand bouten kolom-verankering',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandBoutenKolomVerankering',
                                                           definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandDeurtjeAfschermingen = EMAttribuut(field=StringField,
                                                         naam='toestand deurtje/afschermingen',
                                                         label='toestand deurtje/afschermingen',
                                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandDeurtjeAfschermingen',
                                                         definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandFunderingSeinbrgivs = EMAttribuut(field=StringField,
                                                        naam='toestand fundering (SEINBRGIVS)',
                                                        label='toestand fundering (SEINBRGIVS)',
                                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandFunderingSeinbrgivs',
                                                        definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandLooproosters = EMAttribuut(field=StringField,
                                                 naam='toestand looproosters',
                                                 label='toestand looproosters',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandLooproosters',
                                                 definitie='afhankelijke inspectie eigenschap die enkel maar getoond moet worden als type constructie vakwerk is.keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._toestandSeinbrugIvs = EMAttribuut(field=StringField,
                                                naam='toestand seinbrug IVS',
                                                label='toestand seinbrug IVS',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.toestandSeinbrugIvs',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

        self._typeConstructie = EMAttribuut(field=StringField,
                                            naam='type constructie',
                                            label='type constructie',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.typeConstructie',
                                            definitie='Definitie nog toe te voegen voor eigenschap type constructie')

        self._typeFundering = EMAttribuut(field=StringField,
                                          naam='type fundering',
                                          label='type fundering',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.typeFundering',
                                          definitie='Definitie nog toe te voegen voor eigenschap type fundering')

        self._typeKlemmen = EMAttribuut(field=StringField,
                                        naam='type klemmen',
                                        label='type klemmen',
                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.typeKlemmen',
                                        definitie='Definitie nog toe te voegen voor eigenschap type klemmen')

        self._typeKlemmenblok = EMAttribuut(field=StringField,
                                            naam='type klemmenblok',
                                            label='type klemmenblok',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.typeKlemmenblok',
                                            definitie='Definitie nog toe te voegen voor eigenschap type klemmenblok')

        self._typeOnderhoud = EMAttribuut(field=StringField,
                                          naam='type onderhoud',
                                          label='type onderhoud',
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.typeOnderhoud',
                                          definitie='Definitie nog toe te voegen voor eigenschap type onderhoud')

        self._typeSeinbrug = EMAttribuut(field=StringField,
                                         naam='type seinbrug',
                                         label='type seinbrug',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.typeSeinbrug',
                                         definitie='Definitie nog toe te voegen voor eigenschap type seinbrug')

    @property
    def ralKleurSeinbrgivs(self):
        """tekstveld, mogelijk in te vullen met niet van toepassing of 9070 of andere waarden"""
        return self._ralKleurSeinbrgivs.waarde

    @ralKleurSeinbrgivs.setter
    def ralKleurSeinbrgivs(self, value):
        self._ralKleurSeinbrgivs.set_waarde(value, owner=self)

    @property
    def aantalDeurtjesAfschermingenVervangen(self):
        """Definitie nog toe te voegen voor eigenschap aantal deurtjes/afschermingen vervangen"""
        return self._aantalDeurtjesAfschermingenVervangen.waarde

    @aantalDeurtjesAfschermingenVervangen.setter
    def aantalDeurtjesAfschermingenVervangen(self, value):
        self._aantalDeurtjesAfschermingenVervangen.set_waarde(value, owner=self)

    @property
    def aanwezigheidExtraVerhoog(self):
        """Definitie nog toe te voegen voor eigenschap aanwezigheid extra verhoog"""
        return self._aanwezigheidExtraVerhoog.waarde

    @aanwezigheidExtraVerhoog.setter
    def aanwezigheidExtraVerhoog(self, value):
        self._aanwezigheidExtraVerhoog.set_waarde(value, owner=self)

    @property
    def andereOnderhoudsacties(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._andereOnderhoudsacties.waarde

    @andereOnderhoudsacties.setter
    def andereOnderhoudsacties(self, value):
        self._andereOnderhoudsacties.set_waarde(value, owner=self)

    @property
    def datumNieuweSeinbrugIvs(self):
        """datum waarop de seinbrug IVS geplaatst is"""
        return self._datumNieuweSeinbrugIvs.waarde

    @datumNieuweSeinbrugIvs.setter
    def datumNieuweSeinbrugIvs(self, value):
        self._datumNieuweSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def datumSeinbrugIvsGeschilderd(self):
        """datum waarop seinbrug IVS laatste keer is geschilderd"""
        return self._datumSeinbrugIvsGeschilderd.waarde

    @datumSeinbrugIvsGeschilderd.setter
    def datumSeinbrugIvsGeschilderd(self, value):
        self._datumSeinbrugIvsGeschilderd.set_waarde(value, owner=self)

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
    def geschilderdSeinbrgivs(self):
        """corrosiebescherming geschilderd of niet?"""
        return self._geschilderdSeinbrgivs.waarde

    @geschilderdSeinbrgivs.setter
    def geschilderdSeinbrgivs(self, value):
        self._geschilderdSeinbrgivs.set_waarde(value, owner=self)

    @property
    def interneRoestvorming(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._interneRoestvorming.waarde

    @interneRoestvorming.setter
    def interneRoestvorming(self, value):
        self._interneRoestvorming.set_waarde(value, owner=self)

    @property
    def kabelfout(self):
        """Definitie nog toe te voegen voor eigenschap kabelfout"""
        return self._kabelfout.waarde

    @kabelfout.setter
    def kabelfout(self, value):
        self._kabelfout.set_waarde(value, owner=self)

    @property
    def ladder(self):
        """Definitie nog toe te voegen voor eigenschap ladder"""
        return self._ladder.waarde

    @ladder.setter
    def ladder(self, value):
        self._ladder.set_waarde(value, owner=self)

    @property
    def lengteOverspanningSeinbrgivs(self):
        """lengte overspanning/uitkraging"""
        return self._lengteOverspanningSeinbrgivs.waarde

    @lengteOverspanningSeinbrgivs.setter
    def lengteOverspanningSeinbrgivs(self, value):
        self._lengteOverspanningSeinbrgivs.set_waarde(value, owner=self)

    @property
    def leuningOpDwarsbalk(self):
        """Definitie nog toe te voegen voor eigenschap leuning op dwarsbalk"""
        return self._leuningOpDwarsbalk.waarde

    @leuningOpDwarsbalk.setter
    def leuningOpDwarsbalk(self, value):
        self._leuningOpDwarsbalk.set_waarde(value, owner=self)

    @property
    def minimumVrijeHoogte(self):
        """Definitie nog toe te voegen voor eigenschap minimum vrije hoogte"""
        return self._minimumVrijeHoogte.waarde

    @minimumVrijeHoogte.setter
    def minimumVrijeHoogte(self, value):
        self._minimumVrijeHoogte.set_waarde(value, owner=self)

    @property
    def nummerLeesbaar(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._nummerLeesbaar.waarde

    @nummerLeesbaar.setter
    def nummerLeesbaar(self, value):
        self._nummerLeesbaar.set_waarde(value, owner=self)

    @property
    def opmerkingInventarisSeinbrugIvs(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisSeinbrugIvs.waarde

    @opmerkingInventarisSeinbrugIvs.setter
    def opmerkingInventarisSeinbrugIvs(self, value):
        self._opmerkingInventarisSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def opmerkingToestandSeinbrugIvs(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingToestandSeinbrugIvs.waarde

    @opmerkingToestandSeinbrugIvs.setter
    def opmerkingToestandSeinbrugIvs(self, value):
        self._opmerkingToestandSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def plaatsBeschadigingSeinbrugIvs(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden over de plaats van de beschadiging"""
        return self._plaatsBeschadigingSeinbrugIvs.waarde

    @plaatsBeschadigingSeinbrugIvs.setter
    def plaatsBeschadigingSeinbrugIvs(self, value):
        self._plaatsBeschadigingSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def plaatsExterneRoestvorming(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden over de plaats van de externe roestvorming"""
        return self._plaatsExterneRoestvorming.waarde

    @plaatsExterneRoestvorming.setter
    def plaatsExterneRoestvorming(self, value):
        self._plaatsExterneRoestvorming.set_waarde(value, owner=self)

    @property
    def redenSeinbrugIvsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden seinbrug IVS buiten gebruik"""
        return self._redenSeinbrugIvsBuitenGebruik.waarde

    @redenSeinbrugIvsBuitenGebruik.setter
    def redenSeinbrugIvsBuitenGebruik(self, value):
        self._redenSeinbrugIvsBuitenGebruik.set_waarde(value, owner=self)

    @property
    def reinigingSteunen(self):
        """enkel voor onderhoud IVSB constructies"""
        return self._reinigingSteunen.waarde

    @reinigingSteunen.setter
    def reinigingSteunen(self, value):
        self._reinigingSteunen.set_waarde(value, owner=self)

    @property
    def seinbrugIvsBuitenGebruik(self):
        """indien seinbrug IVS nutteloos is, kan eigenschap buiten gebruik op ja worden gesteld, in afwachting van verwijdering"""
        return self._seinbrugIvsBuitenGebruik.waarde

    @seinbrugIvsBuitenGebruik.setter
    def seinbrugIvsBuitenGebruik(self, value):
        self._seinbrugIvsBuitenGebruik.set_waarde(value, owner=self)

    @property
    def seinbrugTeBehoudenVolgensDienstorder(self):
        """Definitie nog toe te voegen voor eigenschap seinbrug te behouden volgens dienstorder"""
        return self._seinbrugTeBehoudenVolgensDienstorder.waarde

    @seinbrugTeBehoudenVolgensDienstorder.setter
    def seinbrugTeBehoudenVolgensDienstorder(self, value):
        self._seinbrugTeBehoudenVolgensDienstorder.set_waarde(value, owner=self)

    @property
    def toestandBoutenKolomDrager(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandBoutenKolomDrager.waarde

    @toestandBoutenKolomDrager.setter
    def toestandBoutenKolomDrager(self, value):
        self._toestandBoutenKolomDrager.set_waarde(value, owner=self)

    @property
    def toestandBoutenKolomVerankering(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandBoutenKolomVerankering.waarde

    @toestandBoutenKolomVerankering.setter
    def toestandBoutenKolomVerankering(self, value):
        self._toestandBoutenKolomVerankering.set_waarde(value, owner=self)

    @property
    def toestandDeurtjeAfschermingen(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandDeurtjeAfschermingen.waarde

    @toestandDeurtjeAfschermingen.setter
    def toestandDeurtjeAfschermingen(self, value):
        self._toestandDeurtjeAfschermingen.set_waarde(value, owner=self)

    @property
    def toestandFunderingSeinbrgivs(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandFunderingSeinbrgivs.waarde

    @toestandFunderingSeinbrgivs.setter
    def toestandFunderingSeinbrgivs(self, value):
        self._toestandFunderingSeinbrgivs.set_waarde(value, owner=self)

    @property
    def toestandLooproosters(self):
        """afhankelijke inspectie eigenschap die enkel maar getoond moet worden als type constructie vakwerk is.keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandLooproosters.waarde

    @toestandLooproosters.setter
    def toestandLooproosters(self, value):
        self._toestandLooproosters.set_waarde(value, owner=self)

    @property
    def toestandSeinbrugIvs(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._toestandSeinbrugIvs.waarde

    @toestandSeinbrugIvs.setter
    def toestandSeinbrugIvs(self, value):
        self._toestandSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def typeConstructie(self):
        """Definitie nog toe te voegen voor eigenschap type constructie"""
        return self._typeConstructie.waarde

    @typeConstructie.setter
    def typeConstructie(self, value):
        self._typeConstructie.set_waarde(value, owner=self)

    @property
    def typeFundering(self):
        """Definitie nog toe te voegen voor eigenschap type fundering"""
        return self._typeFundering.waarde

    @typeFundering.setter
    def typeFundering(self, value):
        self._typeFundering.set_waarde(value, owner=self)

    @property
    def typeKlemmen(self):
        """Definitie nog toe te voegen voor eigenschap type klemmen"""
        return self._typeKlemmen.waarde

    @typeKlemmen.setter
    def typeKlemmen(self, value):
        self._typeKlemmen.set_waarde(value, owner=self)

    @property
    def typeKlemmenblok(self):
        """Definitie nog toe te voegen voor eigenschap type klemmenblok"""
        return self._typeKlemmenblok.waarde

    @typeKlemmenblok.setter
    def typeKlemmenblok(self, value):
        self._typeKlemmenblok.set_waarde(value, owner=self)

    @property
    def typeOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap type onderhoud"""
        return self._typeOnderhoud.waarde

    @typeOnderhoud.setter
    def typeOnderhoud(self, value):
        self._typeOnderhoud.set_waarde(value, owner=self)

    @property
    def typeSeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type seinbrug"""
        return self._typeSeinbrug.waarde

    @typeSeinbrug.setter
    def typeSeinbrug(self, value):
        self._typeSeinbrug.set_waarde(value, owner=self)

