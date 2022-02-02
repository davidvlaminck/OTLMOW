# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Kast(EMObject):
    """Installatiekast of Voetpadkast - fysieke behuizing"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Kast'
    label = 'Kast'

    def __init__(self):
        super().__init__()

        self._KastBeschadigdFoto = EMAttribuut(field=BooleanField,
                                                 naam='04. kast beschadigd (foto)',
                                                 label='04. kast beschadigd (foto)',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.04KastBeschadigdFoto',
                                                 definitie='Definitie nog toe te voegen voor eigenschap kast beschadigd (foto)')

        self._VervolgActie = EMAttribuut(field=StringField,
                                           naam='09. Vervolg actie',
                                           label='09. Vervolg actie',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.09VervolgActie',
                                           definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._aantalOvbsEnVoetVervangen = EMAttribuut(field=StringField,
                                                      naam='Aantal OVBS en voet vervangen',
                                                      label='Aantal OVBS en voet vervangen',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalOvbsEnVoetVervangen',
                                                      definitie='Definitie nog toe te voegen voor eigenschap Aantal OVBS en voet vervangen')

        self._aantalOvbsVervangen = EMAttribuut(field=StringField,
                                                naam='Aantal OVBS vervangen',
                                                label='Aantal OVBS vervangen',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalOvbsVervangen',
                                                definitie='Definitie nog toe te voegen voor eigenschap Aantal OVBS vervangen')

        self._aantalBuizenAfgedicht = EMAttribuut(field=StringField,
                                                  naam='Aantal buizen afgedicht',
                                                  label='Aantal buizen afgedicht',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.aantalBuizenAfgedicht',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Aantal buizen afgedicht')

        self._aantalBuizenTePlannen = EMAttribuut(field=StringField,
                                                  naam='Aantal buizen te plannen',
                                                  label='Aantal buizen te plannen',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.aantalBuizenTePlannen',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Aantal buizen te plannen')

        self._aantalNogInTePlannen = EMAttribuut(field=StringField,
                                                 naam='Aantal nog in te plannen',
                                                 label='Aantal nog in te plannen',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalNogInTePlannen',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Aantal nog in te plannen')

        self._algemeneOpmerkingen = EMAttribuut(field=StringField,
                                                naam='Algemene opmerkingen',
                                                label='Algemene opmerkingen',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.algemeneOpmerkingen',
                                                definitie='Definitie nog toe te voegen voor eigenschap Algemene opmerkingen')

        self._bekabelingDraadkanalenOrdelijkKast = EMAttribuut(field=StringField,
                                                               naam='Bekabeling/draadkanalen ordelijk (KAST)',
                                                               label='Bekabeling/draadkanalen ordelijk (KAST)',
                                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.bekabelingDraadkanalenOrdelijkKast',
                                                               definitie='Definitie nog toe te voegen voor eigenschap Bekabeling/draadkanalen ordelijk (KAST)')

        self._bereikbaarheidCorrect = EMAttribuut(field=BooleanField,
                                                  naam='Bereikbaarheid correct',
                                                  label='Bereikbaarheid correct',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.bereikbaarheidCorrect',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Bereikbaarheid correct')

        self._betonsokkelGereinigd = EMAttribuut(field=BooleanField,
                                                 naam='Betonsokkel gereinigd',
                                                 label='Betonsokkel gereinigd',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.betonsokkelGereinigd',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Betonsokkel gereinigd')

        self._bezoekficheAanvangtijdstipIngevuld = EMAttribuut(field=BooleanField,
                                                               naam='Bezoekfiche aanvangtijdstip ingevuld',
                                                               label='Bezoekfiche aanvangtijdstip ingevuld',
                                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.bezoekficheAanvangtijdstipIngevuld',
                                                               definitie='Definitie nog toe te voegen voor eigenschap Bezoekfiche aanvangtijdstip ingevuld')

        self._bezoekficheEindtijdstipIngevuld = EMAttribuut(field=BooleanField,
                                                            naam='Bezoekfiche eindtijdstip ingevuld',
                                                            label='Bezoekfiche eindtijdstip ingevuld',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.bezoekficheEindtijdstipIngevuld',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Bezoekfiche eindtijdstip ingevuld')

        self._binnenkantSokkelGestofzuigd = EMAttribuut(field=BooleanField,
                                                        naam='Binnenkant sokkel gestofzuigd',
                                                        label='Binnenkant sokkel gestofzuigd',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.binnenkantSokkelGestofzuigd',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Binnenkant sokkel gestofzuigd')

        self._binnensokkelIsGoedAansluitend = EMAttribuut(field=BooleanField,
                                                          naam='Binnensokkel is goed aansluitend',
                                                          label='Binnensokkel is goed aansluitend',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.binnensokkelIsGoedAansluitend',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Binnensokkel is goed aansluitend')

        self._binnenzijdeGereinigd = EMAttribuut(field=BooleanField,
                                                 naam='Binnenzijde gereinigd',
                                                 label='Binnenzijde gereinigd',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.binnenzijdeGereinigd',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Binnenzijde gereinigd')

        self._buizenZijnGoedAfgedichtKast = EMAttribuut(field=StringField,
                                                        naam='Buizen zijn goed afgedicht (KAST)',
                                                        label='Buizen zijn goed afgedicht (KAST)',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.buizenZijnGoedAfgedichtKast',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Buizen zijn goed afgedicht (KAST)')

        self._deurSluitGoedAf = EMAttribuut(field=BooleanField,
                                            naam='Deur sluit goed af',
                                            label='Deur sluit goed af',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.deurSluitGoedAf',
                                            definitie='Definitie nog toe te voegen voor eigenschap Deur sluit goed af')

        self._deurcontactAanwezig = EMAttribuut(field=BooleanField,
                                                naam='Deurcontact aanwezig',
                                                label='Deurcontact aanwezig',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.deurcontactAanwezig',
                                                definitie='Definitie nog toe te voegen voor eigenschap Deurcontact aanwezig')

        self._eindeKast = EMAttribuut(field=DateTimeField,
                                      naam='Einde (KAST)',
                                      label='Einde (KAST)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.eindeKast',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (KAST)')

        self._filterSVervangen = EMAttribuut(field=BooleanField,
                                             naam='Filter(s) vervangen',
                                             label='Filter(s) vervangen',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.filterSVervangen',
                                             definitie='Definitie nog toe te voegen voor eigenschap Filter(s) vervangen')

        self._fotoVanInhoudVanKastGenomen = EMAttribuut(field=BooleanField,
                                                        naam='Foto van inhoud van kast genomen',
                                                        label='Foto van inhoud van kast genomen',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.fotoVanInhoudVanKastGenomen',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Foto van inhoud van kast genomen')

        self._geldigeKeuringAanwezig = EMAttribuut(field=BooleanField,
                                                   naam='Geldige keuring aanwezig',
                                                   label='Geldige keuring aanwezig',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.geldigeKeuringAanwezig',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Geldige keuring aanwezig')

        self._genaakbareDelenAanwezig = EMAttribuut(field=StringField,
                                                    naam='Genaakbare delen aanwezig',
                                                    label='Genaakbare delen aanwezig',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.genaakbareDelenAanwezig',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Genaakbare delen aanwezig')

        self._graffitiFotoS = EMAttribuut(field=BooleanField,
                                          naam="Graffiti (foto's)",
                                          label="Graffiti (foto's)",
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.graffitiFotoS',
                                          definitie="Definitie nog toe te voegen voor eigenschap Graffiti (foto\'s)")

        self._hebJeGesnoeid = EMAttribuut(field=StringField,
                                          naam='Heb je gesnoeid?',
                                          label='Heb je gesnoeid?',
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.hebJeGesnoeid',
                                          definitie='Definitie nog toe te voegen voor eigenschap Heb je gesnoeid?')

        self._installatienummerAanwezigOpKast = EMAttribuut(field=BooleanField,
                                                            naam='Installatienummer aanwezig op kast',
                                                            label='Installatienummer aanwezig op kast',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.installatienummerAanwezigOpKast',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Installatienummer aanwezig op kast')

        self._isDiffOk = EMAttribuut(field=StringField,
                                     naam='Is diff ok?',
                                     label='Is diff ok?',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.isDiffOk',
                                     definitie='Definitie nog toe te voegen voor eigenschap Is diff ok?')

        self._k04VervolgActie = EMAttribuut(field=StringField,
                                            naam='K04. Vervolg actie',
                                            label='K04. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.k04VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._k20VervolgActie = EMAttribuut(field=StringField,
                                            naam='K20. Vervolg actie',
                                            label='K20. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.k20VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._k24VervolgActie = EMAttribuut(field=StringField,
                                            naam='K24. Vervolg actie',
                                            label='K24. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.k24VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._k28VervolgActie = EMAttribuut(field=StringField,
                                            naam='K28. Vervolg actie',
                                            label='K28. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.k28VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._kastVlotToegankelijkBeplanting = EMAttribuut(field=StringField,
                                                           naam='Kast vlot toegankelijk (beplanting)',
                                                           label='Kast vlot toegankelijk (beplanting)',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.kastVlotToegankelijkBeplanting',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Kast vlot toegankelijk (beplanting)')

        self._knaagdierenbestrijding = EMAttribuut(field=BooleanField,
                                                   naam='Knaagdierenbestrijding',
                                                   label='Knaagdierenbestrijding',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.knaagdierenbestrijding',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Knaagdierenbestrijding')

        self._labelingElektrischeOnderdelenOkKast = EMAttribuut(field=StringField,
                                                                naam='Labeling elektrische onderdelen OK (KAST)',
                                                                label='Labeling elektrische onderdelen OK (KAST)',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.labelingElektrischeOnderdelenOkKast',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Labeling elektrische onderdelen OK (KAST)')

        self._omschrijvingAanpassing = EMAttribuut(field=StringField,
                                                   naam='Omschrijving aanpassing',
                                                   label='Omschrijving aanpassing',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.omschrijvingAanpassing',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Omschrijving aanpassing')

        self._omschrijvingBeschadiging = EMAttribuut(field=StringField,
                                                     naam='Omschrijving beschadiging',
                                                     label='Omschrijving beschadiging',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.omschrijvingBeschadiging',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Omschrijving beschadiging')

        self._omschrijvingPlanning = EMAttribuut(field=StringField,
                                                 naam='Omschrijving planning',
                                                 label='Omschrijving planning',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.omschrijvingPlanning',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Omschrijving planning')

        self._omschrijvingWaarKmp = EMAttribuut(field=StringField,
                                                naam='Omschrijving waar? KMP?',
                                                label='Omschrijving waar? KMP?',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.omschrijvingWaarKmp',
                                                definitie='Definitie nog toe te voegen voor eigenschap Omschrijving waar? KMP?')

        self._overspanningsBeveiligingenOk = EMAttribuut(field=BooleanField,
                                                         naam='Overspannings beveiligingen OK',
                                                         label='Overspannings beveiligingen OK',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.overspanningsBeveiligingenOk',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Overspannings beveiligingen OK')

        self._plantenEnOfOngedierteVerwijderd = EMAttribuut(field=BooleanField,
                                                            naam='Planten en/of ongedierte verwijderd',
                                                            label='Planten en/of ongedierte verwijderd',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.plantenEnOfOngedierteVerwijderd',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Planten en/of ongedierte verwijderd')

        self._reinigenBuitenzijdeKast = EMAttribuut(field=BooleanField,
                                                    naam='Reinigen buitenzijde kast',
                                                    label='Reinigen buitenzijde kast',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.reinigenBuitenzijdeKast',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Reinigen buitenzijde kast')

        self._schroevenContactenOkSteekproef = EMAttribuut(field=BooleanField,
                                                           naam='Schroeven contacten ok (steekproef)',
                                                           label='Schroeven contacten ok (steekproef)',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.schroevenContactenOkSteekproef',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Schroeven contacten ok (steekproef)')

        self._slotGesmeerdEnGereinigd = EMAttribuut(field=BooleanField,
                                                    naam='Slot gesmeerd en gereinigd',
                                                    label='Slot gesmeerd en gereinigd',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.slotGesmeerdEnGereinigd',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Slot gesmeerd en gereinigd')

        self._startBezoek = EMAttribuut(field=DateTimeField,
                                        naam='Start bezoek',
                                        label='Start bezoek',
                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.startBezoek',
                                        definitie='Definitie nog toe te voegen voor eigenschap Start bezoek')

        self._stekkersGecontroleerd = EMAttribuut(field=BooleanField,
                                                  naam='Stekkers gecontroleerd',
                                                  label='Stekkers gecontroleerd',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.stekkersGecontroleerd',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Stekkers gecontroleerd')

        self._vtcSticker = EMAttribuut(field=BooleanField,
                                       naam='VTC-sticker',
                                       label='VTC-sticker',
                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.vtcSticker',
                                       definitie='Definitie nog toe te voegen voor eigenschap VTC-sticker')

        self._ventilatieOpeningenAppGestofzuigd = EMAttribuut(field=BooleanField,
                                                              naam='Ventilatie-openingen app gestofzuigd',
                                                              label='Ventilatie-openingen app gestofzuigd',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.ventilatieOpeningenAppGestofzuigd',
                                                              definitie='Definitie nog toe te voegen voor eigenschap Ventilatie-openingen app gestofzuigd')

        self._werkingDiffGetestViaTestknop = EMAttribuut(field=BooleanField,
                                                         naam='Werking diff getest (via testknop)',
                                                         label='Werking diff getest (via testknop)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.werkingDiffGetestViaTestknop',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Werking diff getest (via testknop)')

        self._werkingKastventilatieOkKast = EMAttribuut(field=StringField,
                                                        naam='Werking kastventilatie OK (KAST)',
                                                        label='Werking kastventilatie OK (KAST)',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.werkingKastventilatieOkKast',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Werking kastventilatie OK (KAST)')

        self._werkingKastverlichtingOkKast = EMAttribuut(field=StringField,
                                                         naam='Werking kastverlichting OK (KAST)',
                                                         label='Werking kastverlichting OK (KAST)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.werkingKastverlichtingOkKast',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Werking kastverlichting OK (KAST)')

        self._werkingKastverwarmingOkKast = EMAttribuut(field=StringField,
                                                        naam='Werking kastverwarming OK (KAST)',
                                                        label='Werking kastverwarming OK (KAST)',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Kast.werkingKastverwarmingOkKast',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Werking kastverwarming OK (KAST)')

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie')

    @property
    def KastBeschadigdFoto(self):
        """Definitie nog toe te voegen voor eigenschap kast beschadigd (foto)"""
        return self._KastBeschadigdFoto.waarde

    @KastBeschadigdFoto.setter
    def KastBeschadigdFoto(self, value):
        self._KastBeschadigdFoto.set_waarde(value, owner=self)

    @property
    def VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._VervolgActie.waarde

    @VervolgActie.setter
    def VervolgActie(self, value):
        self._VervolgActie.set_waarde(value, owner=self)

    @property
    def aantalOvbsEnVoetVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Aantal OVBS en voet vervangen"""
        return self._aantalOvbsEnVoetVervangen.waarde

    @aantalOvbsEnVoetVervangen.setter
    def aantalOvbsEnVoetVervangen(self, value):
        self._aantalOvbsEnVoetVervangen.set_waarde(value, owner=self)

    @property
    def aantalOvbsVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Aantal OVBS vervangen"""
        return self._aantalOvbsVervangen.waarde

    @aantalOvbsVervangen.setter
    def aantalOvbsVervangen(self, value):
        self._aantalOvbsVervangen.set_waarde(value, owner=self)

    @property
    def aantalBuizenAfgedicht(self):
        """Definitie nog toe te voegen voor eigenschap Aantal buizen afgedicht"""
        return self._aantalBuizenAfgedicht.waarde

    @aantalBuizenAfgedicht.setter
    def aantalBuizenAfgedicht(self, value):
        self._aantalBuizenAfgedicht.set_waarde(value, owner=self)

    @property
    def aantalBuizenTePlannen(self):
        """Definitie nog toe te voegen voor eigenschap Aantal buizen te plannen"""
        return self._aantalBuizenTePlannen.waarde

    @aantalBuizenTePlannen.setter
    def aantalBuizenTePlannen(self, value):
        self._aantalBuizenTePlannen.set_waarde(value, owner=self)

    @property
    def aantalNogInTePlannen(self):
        """Definitie nog toe te voegen voor eigenschap Aantal nog in te plannen"""
        return self._aantalNogInTePlannen.waarde

    @aantalNogInTePlannen.setter
    def aantalNogInTePlannen(self, value):
        self._aantalNogInTePlannen.set_waarde(value, owner=self)

    @property
    def algemeneOpmerkingen(self):
        """Definitie nog toe te voegen voor eigenschap Algemene opmerkingen"""
        return self._algemeneOpmerkingen.waarde

    @algemeneOpmerkingen.setter
    def algemeneOpmerkingen(self, value):
        self._algemeneOpmerkingen.set_waarde(value, owner=self)

    @property
    def bekabelingDraadkanalenOrdelijkKast(self):
        """Definitie nog toe te voegen voor eigenschap Bekabeling/draadkanalen ordelijk (KAST)"""
        return self._bekabelingDraadkanalenOrdelijkKast.waarde

    @bekabelingDraadkanalenOrdelijkKast.setter
    def bekabelingDraadkanalenOrdelijkKast(self, value):
        self._bekabelingDraadkanalenOrdelijkKast.set_waarde(value, owner=self)

    @property
    def bereikbaarheidCorrect(self):
        """Definitie nog toe te voegen voor eigenschap Bereikbaarheid correct"""
        return self._bereikbaarheidCorrect.waarde

    @bereikbaarheidCorrect.setter
    def bereikbaarheidCorrect(self, value):
        self._bereikbaarheidCorrect.set_waarde(value, owner=self)

    @property
    def betonsokkelGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Betonsokkel gereinigd"""
        return self._betonsokkelGereinigd.waarde

    @betonsokkelGereinigd.setter
    def betonsokkelGereinigd(self, value):
        self._betonsokkelGereinigd.set_waarde(value, owner=self)

    @property
    def bezoekficheAanvangtijdstipIngevuld(self):
        """Definitie nog toe te voegen voor eigenschap Bezoekfiche aanvangtijdstip ingevuld"""
        return self._bezoekficheAanvangtijdstipIngevuld.waarde

    @bezoekficheAanvangtijdstipIngevuld.setter
    def bezoekficheAanvangtijdstipIngevuld(self, value):
        self._bezoekficheAanvangtijdstipIngevuld.set_waarde(value, owner=self)

    @property
    def bezoekficheEindtijdstipIngevuld(self):
        """Definitie nog toe te voegen voor eigenschap Bezoekfiche eindtijdstip ingevuld"""
        return self._bezoekficheEindtijdstipIngevuld.waarde

    @bezoekficheEindtijdstipIngevuld.setter
    def bezoekficheEindtijdstipIngevuld(self, value):
        self._bezoekficheEindtijdstipIngevuld.set_waarde(value, owner=self)

    @property
    def binnenkantSokkelGestofzuigd(self):
        """Definitie nog toe te voegen voor eigenschap Binnenkant sokkel gestofzuigd"""
        return self._binnenkantSokkelGestofzuigd.waarde

    @binnenkantSokkelGestofzuigd.setter
    def binnenkantSokkelGestofzuigd(self, value):
        self._binnenkantSokkelGestofzuigd.set_waarde(value, owner=self)

    @property
    def binnensokkelIsGoedAansluitend(self):
        """Definitie nog toe te voegen voor eigenschap Binnensokkel is goed aansluitend"""
        return self._binnensokkelIsGoedAansluitend.waarde

    @binnensokkelIsGoedAansluitend.setter
    def binnensokkelIsGoedAansluitend(self, value):
        self._binnensokkelIsGoedAansluitend.set_waarde(value, owner=self)

    @property
    def binnenzijdeGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Binnenzijde gereinigd"""
        return self._binnenzijdeGereinigd.waarde

    @binnenzijdeGereinigd.setter
    def binnenzijdeGereinigd(self, value):
        self._binnenzijdeGereinigd.set_waarde(value, owner=self)

    @property
    def buizenZijnGoedAfgedichtKast(self):
        """Definitie nog toe te voegen voor eigenschap Buizen zijn goed afgedicht (KAST)"""
        return self._buizenZijnGoedAfgedichtKast.waarde

    @buizenZijnGoedAfgedichtKast.setter
    def buizenZijnGoedAfgedichtKast(self, value):
        self._buizenZijnGoedAfgedichtKast.set_waarde(value, owner=self)

    @property
    def deurSluitGoedAf(self):
        """Definitie nog toe te voegen voor eigenschap Deur sluit goed af"""
        return self._deurSluitGoedAf.waarde

    @deurSluitGoedAf.setter
    def deurSluitGoedAf(self, value):
        self._deurSluitGoedAf.set_waarde(value, owner=self)

    @property
    def deurcontactAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap Deurcontact aanwezig"""
        return self._deurcontactAanwezig.waarde

    @deurcontactAanwezig.setter
    def deurcontactAanwezig(self, value):
        self._deurcontactAanwezig.set_waarde(value, owner=self)

    @property
    def eindeKast(self):
        """Definitie nog toe te voegen voor eigenschap Einde (KAST)"""
        return self._eindeKast.waarde

    @eindeKast.setter
    def eindeKast(self, value):
        self._eindeKast.set_waarde(value, owner=self)

    @property
    def filterSVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Filter(s) vervangen"""
        return self._filterSVervangen.waarde

    @filterSVervangen.setter
    def filterSVervangen(self, value):
        self._filterSVervangen.set_waarde(value, owner=self)

    @property
    def fotoVanInhoudVanKastGenomen(self):
        """Definitie nog toe te voegen voor eigenschap Foto van inhoud van kast genomen"""
        return self._fotoVanInhoudVanKastGenomen.waarde

    @fotoVanInhoudVanKastGenomen.setter
    def fotoVanInhoudVanKastGenomen(self, value):
        self._fotoVanInhoudVanKastGenomen.set_waarde(value, owner=self)

    @property
    def geldigeKeuringAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap Geldige keuring aanwezig"""
        return self._geldigeKeuringAanwezig.waarde

    @geldigeKeuringAanwezig.setter
    def geldigeKeuringAanwezig(self, value):
        self._geldigeKeuringAanwezig.set_waarde(value, owner=self)

    @property
    def genaakbareDelenAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap Genaakbare delen aanwezig"""
        return self._genaakbareDelenAanwezig.waarde

    @genaakbareDelenAanwezig.setter
    def genaakbareDelenAanwezig(self, value):
        self._genaakbareDelenAanwezig.set_waarde(value, owner=self)

    @property
    def graffitiFotoS(self):
        """Definitie nog toe te voegen voor eigenschap Graffiti (foto\'s)"""
        return self._graffitiFotoS.waarde

    @graffitiFotoS.setter
    def graffitiFotoS(self, value):
        self._graffitiFotoS.set_waarde(value, owner=self)

    @property
    def hebJeGesnoeid(self):
        """Definitie nog toe te voegen voor eigenschap Heb je gesnoeid?"""
        return self._hebJeGesnoeid.waarde

    @hebJeGesnoeid.setter
    def hebJeGesnoeid(self, value):
        self._hebJeGesnoeid.set_waarde(value, owner=self)

    @property
    def installatienummerAanwezigOpKast(self):
        """Definitie nog toe te voegen voor eigenschap Installatienummer aanwezig op kast"""
        return self._installatienummerAanwezigOpKast.waarde

    @installatienummerAanwezigOpKast.setter
    def installatienummerAanwezigOpKast(self, value):
        self._installatienummerAanwezigOpKast.set_waarde(value, owner=self)

    @property
    def isDiffOk(self):
        """Definitie nog toe te voegen voor eigenschap Is diff ok?"""
        return self._isDiffOk.waarde

    @isDiffOk.setter
    def isDiffOk(self, value):
        self._isDiffOk.set_waarde(value, owner=self)

    @property
    def k04VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._k04VervolgActie.waarde

    @k04VervolgActie.setter
    def k04VervolgActie(self, value):
        self._k04VervolgActie.set_waarde(value, owner=self)

    @property
    def k20VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._k20VervolgActie.waarde

    @k20VervolgActie.setter
    def k20VervolgActie(self, value):
        self._k20VervolgActie.set_waarde(value, owner=self)

    @property
    def k24VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._k24VervolgActie.waarde

    @k24VervolgActie.setter
    def k24VervolgActie(self, value):
        self._k24VervolgActie.set_waarde(value, owner=self)

    @property
    def k28VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._k28VervolgActie.waarde

    @k28VervolgActie.setter
    def k28VervolgActie(self, value):
        self._k28VervolgActie.set_waarde(value, owner=self)

    @property
    def kastVlotToegankelijkBeplanting(self):
        """Definitie nog toe te voegen voor eigenschap Kast vlot toegankelijk (beplanting)"""
        return self._kastVlotToegankelijkBeplanting.waarde

    @kastVlotToegankelijkBeplanting.setter
    def kastVlotToegankelijkBeplanting(self, value):
        self._kastVlotToegankelijkBeplanting.set_waarde(value, owner=self)

    @property
    def knaagdierenbestrijding(self):
        """Definitie nog toe te voegen voor eigenschap Knaagdierenbestrijding"""
        return self._knaagdierenbestrijding.waarde

    @knaagdierenbestrijding.setter
    def knaagdierenbestrijding(self, value):
        self._knaagdierenbestrijding.set_waarde(value, owner=self)

    @property
    def labelingElektrischeOnderdelenOkKast(self):
        """Definitie nog toe te voegen voor eigenschap Labeling elektrische onderdelen OK (KAST)"""
        return self._labelingElektrischeOnderdelenOkKast.waarde

    @labelingElektrischeOnderdelenOkKast.setter
    def labelingElektrischeOnderdelenOkKast(self, value):
        self._labelingElektrischeOnderdelenOkKast.set_waarde(value, owner=self)

    @property
    def omschrijvingAanpassing(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijving aanpassing"""
        return self._omschrijvingAanpassing.waarde

    @omschrijvingAanpassing.setter
    def omschrijvingAanpassing(self, value):
        self._omschrijvingAanpassing.set_waarde(value, owner=self)

    @property
    def omschrijvingBeschadiging(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijving beschadiging"""
        return self._omschrijvingBeschadiging.waarde

    @omschrijvingBeschadiging.setter
    def omschrijvingBeschadiging(self, value):
        self._omschrijvingBeschadiging.set_waarde(value, owner=self)

    @property
    def omschrijvingPlanning(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijving planning"""
        return self._omschrijvingPlanning.waarde

    @omschrijvingPlanning.setter
    def omschrijvingPlanning(self, value):
        self._omschrijvingPlanning.set_waarde(value, owner=self)

    @property
    def omschrijvingWaarKmp(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijving waar? KMP?"""
        return self._omschrijvingWaarKmp.waarde

    @omschrijvingWaarKmp.setter
    def omschrijvingWaarKmp(self, value):
        self._omschrijvingWaarKmp.set_waarde(value, owner=self)

    @property
    def overspanningsBeveiligingenOk(self):
        """Definitie nog toe te voegen voor eigenschap Overspannings beveiligingen OK"""
        return self._overspanningsBeveiligingenOk.waarde

    @overspanningsBeveiligingenOk.setter
    def overspanningsBeveiligingenOk(self, value):
        self._overspanningsBeveiligingenOk.set_waarde(value, owner=self)

    @property
    def plantenEnOfOngedierteVerwijderd(self):
        """Definitie nog toe te voegen voor eigenschap Planten en/of ongedierte verwijderd"""
        return self._plantenEnOfOngedierteVerwijderd.waarde

    @plantenEnOfOngedierteVerwijderd.setter
    def plantenEnOfOngedierteVerwijderd(self, value):
        self._plantenEnOfOngedierteVerwijderd.set_waarde(value, owner=self)

    @property
    def reinigenBuitenzijdeKast(self):
        """Definitie nog toe te voegen voor eigenschap Reinigen buitenzijde kast"""
        return self._reinigenBuitenzijdeKast.waarde

    @reinigenBuitenzijdeKast.setter
    def reinigenBuitenzijdeKast(self, value):
        self._reinigenBuitenzijdeKast.set_waarde(value, owner=self)

    @property
    def schroevenContactenOkSteekproef(self):
        """Definitie nog toe te voegen voor eigenschap Schroeven contacten ok (steekproef)"""
        return self._schroevenContactenOkSteekproef.waarde

    @schroevenContactenOkSteekproef.setter
    def schroevenContactenOkSteekproef(self, value):
        self._schroevenContactenOkSteekproef.set_waarde(value, owner=self)

    @property
    def slotGesmeerdEnGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Slot gesmeerd en gereinigd"""
        return self._slotGesmeerdEnGereinigd.waarde

    @slotGesmeerdEnGereinigd.setter
    def slotGesmeerdEnGereinigd(self, value):
        self._slotGesmeerdEnGereinigd.set_waarde(value, owner=self)

    @property
    def startBezoek(self):
        """Definitie nog toe te voegen voor eigenschap Start bezoek"""
        return self._startBezoek.waarde

    @startBezoek.setter
    def startBezoek(self, value):
        self._startBezoek.set_waarde(value, owner=self)

    @property
    def stekkersGecontroleerd(self):
        """Definitie nog toe te voegen voor eigenschap Stekkers gecontroleerd"""
        return self._stekkersGecontroleerd.waarde

    @stekkersGecontroleerd.setter
    def stekkersGecontroleerd(self, value):
        self._stekkersGecontroleerd.set_waarde(value, owner=self)

    @property
    def vtcSticker(self):
        """Definitie nog toe te voegen voor eigenschap VTC-sticker"""
        return self._vtcSticker.waarde

    @vtcSticker.setter
    def vtcSticker(self, value):
        self._vtcSticker.set_waarde(value, owner=self)

    @property
    def ventilatieOpeningenAppGestofzuigd(self):
        """Definitie nog toe te voegen voor eigenschap Ventilatie-openingen app gestofzuigd"""
        return self._ventilatieOpeningenAppGestofzuigd.waarde

    @ventilatieOpeningenAppGestofzuigd.setter
    def ventilatieOpeningenAppGestofzuigd(self, value):
        self._ventilatieOpeningenAppGestofzuigd.set_waarde(value, owner=self)

    @property
    def werkingDiffGetestViaTestknop(self):
        """Definitie nog toe te voegen voor eigenschap Werking diff getest (via testknop)"""
        return self._werkingDiffGetestViaTestknop.waarde

    @werkingDiffGetestViaTestknop.setter
    def werkingDiffGetestViaTestknop(self, value):
        self._werkingDiffGetestViaTestknop.set_waarde(value, owner=self)

    @property
    def werkingKastventilatieOkKast(self):
        """Definitie nog toe te voegen voor eigenschap Werking kastventilatie OK (KAST)"""
        return self._werkingKastventilatieOkKast.waarde

    @werkingKastventilatieOkKast.setter
    def werkingKastventilatieOkKast(self, value):
        self._werkingKastventilatieOkKast.set_waarde(value, owner=self)

    @property
    def werkingKastverlichtingOkKast(self):
        """Definitie nog toe te voegen voor eigenschap Werking kastverlichting OK (KAST)"""
        return self._werkingKastverlichtingOkKast.waarde

    @werkingKastverlichtingOkKast.setter
    def werkingKastverlichtingOkKast(self, value):
        self._werkingKastverlichtingOkKast.set_waarde(value, owner=self)

    @property
    def werkingKastverwarmingOkKast(self):
        """Definitie nog toe te voegen voor eigenschap Werking kastverwarming OK (KAST)"""
        return self._werkingKastverwarmingOkKast.waarde

    @werkingKastverwarmingOkKast.setter
    def werkingKastverwarmingOkKast(self, value):
        self._werkingKastverwarmingOkKast.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

