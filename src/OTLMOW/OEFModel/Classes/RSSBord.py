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

        self._aantalNogInTePlannen = EMAttribuut(field=StringField,
                                                 naam='Aantal nog in te plannen',
                                                 label='Aantal nog in te plannen',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aantalNogInTePlannen',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Aantal nog in te plannen')

        self._b07VervolgActie = EMAttribuut(field=StringField,
                                            naam='B07. Vervolg actie',
                                            label='B07. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.b07VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._b08VervolgActie = EMAttribuut(field=StringField,
                                            naam='B08. Vervolg actie',
                                            label='B08. Vervolg actie',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#RSSBord.b08VervolgActie',
                                            definitie='Definitie nog toe te voegen voor eigenschap Vervolg actie')

        self._binnenzijdeBordGereinigd = EMAttribuut(field=BooleanField,
                                                     naam='Binnenzijde bord gereinigd',
                                                     label='Binnenzijde bord gereinigd',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.binnenzijdeBordGereinigd',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Binnenzijde bord gereinigd')

        self._bordbevestigingInGoedeStaatFoto = EMAttribuut(field=StringField,
                                                            naam='Bordbevestiging in goede staat(foto)',
                                                            label='Bordbevestiging in goede staat(foto)',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.bordbevestigingInGoedeStaatFoto',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Bordbevestiging in goede staat(foto)')

        self._deurcontactInOrde = EMAttribuut(field=StringField,
                                              naam='Deurcontact in orde',
                                              label='Deurcontact in orde',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.deurcontactInOrde',
                                              definitie='Definitie nog toe te voegen voor eigenschap Deurcontact in orde')

        self._filtermattenGereinigdVervangen = EMAttribuut(field=BooleanField,
                                                           naam='Filtermatten gereinigd / vervangen',
                                                           label='Filtermatten gereinigd / vervangen',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.filtermattenGereinigdVervangen',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Filtermatten gereinigd / vervangen')

        self._goedeWerkingBordEn = EMAttribuut(field=StringField,
                                               naam='Goede werking bord(en)',
                                               label='Goede werking bord(en)',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.goedeWerkingBordEn',
                                               definitie='Definitie nog toe te voegen voor eigenschap Goede werking bord(en)')

        self._graffitiAanwezigFoto = EMAttribuut(field=BooleanField,
                                                 naam='Graffiti aanwezig (foto)',
                                                 label='Graffiti aanwezig (foto)',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.graffitiAanwezigFoto',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Graffiti aanwezig (foto)')

        self._infoHerstellingBord = EMAttribuut(field=StringField,
                                                naam='Info herstelling bord',
                                                label='Info herstelling bord',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.infoHerstellingBord',
                                                definitie='Definitie nog toe te voegen voor eigenschap Info herstelling bord')

        self._infoTePlannen = EMAttribuut(field=StringField,
                                          naam='Info te plannen',
                                          label='Info te plannen',
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.infoTePlannen',
                                          definitie='Definitie nog toe te voegen voor eigenschap Info te plannen')

        self._isDiffInOrde = EMAttribuut(field=BooleanField,
                                         naam='Is diff in orde?',
                                         label='Is diff in orde?',
                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.isDiffInOrde',
                                         definitie='Definitie nog toe te voegen voor eigenschap Is diff in orde?')

        self._kabelinvoerenInOrde = EMAttribuut(field=StringField,
                                                naam='Kabelinvoeren in orde',
                                                label='Kabelinvoeren in orde',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.kabelinvoerenInOrde',
                                                definitie='Definitie nog toe te voegen voor eigenschap Kabelinvoeren in orde')

        self._ledprintsGoedBevestigd = EMAttribuut(field=StringField,
                                                   naam='Ledprints goed bevestigd',
                                                   label='Ledprints goed bevestigd',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.ledprintsGoedBevestigd',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Ledprints goed bevestigd')

        self._lichtsensorVrijgemaakt = EMAttribuut(field=StringField,
                                                   naam='Lichtsensor vrijgemaakt',
                                                   label='Lichtsensor vrijgemaakt',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.lichtsensorVrijgemaakt',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Lichtsensor vrijgemaakt')

        self._lichtsensorenInOrde = EMAttribuut(field=StringField,
                                                naam='Lichtsensoren in orde',
                                                label='Lichtsensoren in orde',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.lichtsensorenInOrde',
                                                definitie='Definitie nog toe te voegen voor eigenschap Lichtsensoren in orde')

        self._luchtfiltersGereinigd = EMAttribuut(field=BooleanField,
                                                  naam='Luchtfilters gereinigd',
                                                  label='Luchtfilters gereinigd',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.luchtfiltersGereinigd',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Luchtfilters gereinigd')

        self._ordentelijkeInterneBekabeling = EMAttribuut(field=StringField,
                                                          naam='Ordentelijke interne bekabeling',
                                                          label='Ordentelijke interne bekabeling',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.ordentelijkeInterneBekabeling',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Ordentelijke interne bekabeling')

        self._overspanningsbeveiligingInOrde = EMAttribuut(field=BooleanField,
                                                           naam='Overspanningsbeveiliging in orde',
                                                           label='Overspanningsbeveiliging in orde',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.overspanningsbeveiligingInOrde',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Overspanningsbeveiliging in orde')

        self._rssBuitenGebruik = EMAttribuut(field=BooleanField,
                                             naam='RSS buiten gebruik',
                                             label='RSS buiten gebruik',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RSSBord.rssBuitenGebruik',
                                             definitie='Definitie nog toe te voegen voor eigenschap RSS buiten gebruik')

        self._reinigenBordNoodzakelijkFoto = EMAttribuut(field=BooleanField,
                                                         naam='Reinigen bord noodzakelijk (foto)',
                                                         label='Reinigen bord noodzakelijk (foto)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.reinigenBordNoodzakelijkFoto',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Reinigen bord noodzakelijk (foto)')

        self._verlichtingInOrde = EMAttribuut(field=StringField,
                                              naam='Verlichting in orde',
                                              label='Verlichting in orde',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingInOrde',
                                              definitie='Definitie nog toe te voegen voor eigenschap Verlichting in orde')

        self._vervangenLuchtfilterS = EMAttribuut(field=StringField,
                                                  naam='Vervangen luchtfilter(s)',
                                                  label='Vervangen luchtfilter(s)',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.vervangenLuchtfilterS',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Vervangen luchtfilter(s)')

        self._verwarmingEnVerluchtingInOrde = EMAttribuut(field=StringField,
                                                          naam='Verwarming en verluchting in orde',
                                                          label='Verwarming en verluchting in orde',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.verwarmingEnVerluchtingInOrde',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Verwarming en verluchting in orde')

        self._waterdichtheidBordInOrde = EMAttribuut(field=StringField,
                                                     naam='Waterdichtheid bord in orde',
                                                     label='Waterdichtheid bord in orde',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.waterdichtheidBordInOrde',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Waterdichtheid bord in orde')

        self._werkingDiffGetestViaTestknop = EMAttribuut(field=BooleanField,
                                                         naam='Werking diff getest (via testknop)',
                                                         label='Werking diff getest (via testknop)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.werkingDiffGetestViaTestknop',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Werking diff getest (via testknop)')

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

        self._toestandRssBord = EMAttribuut(field=StringField,
                                            naam='toestand RSS bord',
                                            label='toestand RSS bord',
                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#RSSBord.toestandRssBord',
                                            definitie='Definitie nog toe te voegen voor eigenschap toestand RSS bord')

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
    def aantalNogInTePlannen(self):
        """Definitie nog toe te voegen voor eigenschap Aantal nog in te plannen"""
        return self._aantalNogInTePlannen.waarde

    @aantalNogInTePlannen.setter
    def aantalNogInTePlannen(self, value):
        self._aantalNogInTePlannen.set_waarde(value, owner=self)

    @property
    def b07VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._b07VervolgActie.waarde

    @b07VervolgActie.setter
    def b07VervolgActie(self, value):
        self._b07VervolgActie.set_waarde(value, owner=self)

    @property
    def b08VervolgActie(self):
        """Definitie nog toe te voegen voor eigenschap Vervolg actie"""
        return self._b08VervolgActie.waarde

    @b08VervolgActie.setter
    def b08VervolgActie(self, value):
        self._b08VervolgActie.set_waarde(value, owner=self)

    @property
    def binnenzijdeBordGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Binnenzijde bord gereinigd"""
        return self._binnenzijdeBordGereinigd.waarde

    @binnenzijdeBordGereinigd.setter
    def binnenzijdeBordGereinigd(self, value):
        self._binnenzijdeBordGereinigd.set_waarde(value, owner=self)

    @property
    def bordbevestigingInGoedeStaatFoto(self):
        """Definitie nog toe te voegen voor eigenschap Bordbevestiging in goede staat(foto)"""
        return self._bordbevestigingInGoedeStaatFoto.waarde

    @bordbevestigingInGoedeStaatFoto.setter
    def bordbevestigingInGoedeStaatFoto(self, value):
        self._bordbevestigingInGoedeStaatFoto.set_waarde(value, owner=self)

    @property
    def deurcontactInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Deurcontact in orde"""
        return self._deurcontactInOrde.waarde

    @deurcontactInOrde.setter
    def deurcontactInOrde(self, value):
        self._deurcontactInOrde.set_waarde(value, owner=self)

    @property
    def filtermattenGereinigdVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Filtermatten gereinigd / vervangen"""
        return self._filtermattenGereinigdVervangen.waarde

    @filtermattenGereinigdVervangen.setter
    def filtermattenGereinigdVervangen(self, value):
        self._filtermattenGereinigdVervangen.set_waarde(value, owner=self)

    @property
    def goedeWerkingBordEn(self):
        """Definitie nog toe te voegen voor eigenschap Goede werking bord(en)"""
        return self._goedeWerkingBordEn.waarde

    @goedeWerkingBordEn.setter
    def goedeWerkingBordEn(self, value):
        self._goedeWerkingBordEn.set_waarde(value, owner=self)

    @property
    def graffitiAanwezigFoto(self):
        """Definitie nog toe te voegen voor eigenschap Graffiti aanwezig (foto)"""
        return self._graffitiAanwezigFoto.waarde

    @graffitiAanwezigFoto.setter
    def graffitiAanwezigFoto(self, value):
        self._graffitiAanwezigFoto.set_waarde(value, owner=self)

    @property
    def infoHerstellingBord(self):
        """Definitie nog toe te voegen voor eigenschap Info herstelling bord"""
        return self._infoHerstellingBord.waarde

    @infoHerstellingBord.setter
    def infoHerstellingBord(self, value):
        self._infoHerstellingBord.set_waarde(value, owner=self)

    @property
    def infoTePlannen(self):
        """Definitie nog toe te voegen voor eigenschap Info te plannen"""
        return self._infoTePlannen.waarde

    @infoTePlannen.setter
    def infoTePlannen(self, value):
        self._infoTePlannen.set_waarde(value, owner=self)

    @property
    def isDiffInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Is diff in orde?"""
        return self._isDiffInOrde.waarde

    @isDiffInOrde.setter
    def isDiffInOrde(self, value):
        self._isDiffInOrde.set_waarde(value, owner=self)

    @property
    def kabelinvoerenInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Kabelinvoeren in orde"""
        return self._kabelinvoerenInOrde.waarde

    @kabelinvoerenInOrde.setter
    def kabelinvoerenInOrde(self, value):
        self._kabelinvoerenInOrde.set_waarde(value, owner=self)

    @property
    def ledprintsGoedBevestigd(self):
        """Definitie nog toe te voegen voor eigenschap Ledprints goed bevestigd"""
        return self._ledprintsGoedBevestigd.waarde

    @ledprintsGoedBevestigd.setter
    def ledprintsGoedBevestigd(self, value):
        self._ledprintsGoedBevestigd.set_waarde(value, owner=self)

    @property
    def lichtsensorVrijgemaakt(self):
        """Definitie nog toe te voegen voor eigenschap Lichtsensor vrijgemaakt"""
        return self._lichtsensorVrijgemaakt.waarde

    @lichtsensorVrijgemaakt.setter
    def lichtsensorVrijgemaakt(self, value):
        self._lichtsensorVrijgemaakt.set_waarde(value, owner=self)

    @property
    def lichtsensorenInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Lichtsensoren in orde"""
        return self._lichtsensorenInOrde.waarde

    @lichtsensorenInOrde.setter
    def lichtsensorenInOrde(self, value):
        self._lichtsensorenInOrde.set_waarde(value, owner=self)

    @property
    def luchtfiltersGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Luchtfilters gereinigd"""
        return self._luchtfiltersGereinigd.waarde

    @luchtfiltersGereinigd.setter
    def luchtfiltersGereinigd(self, value):
        self._luchtfiltersGereinigd.set_waarde(value, owner=self)

    @property
    def ordentelijkeInterneBekabeling(self):
        """Definitie nog toe te voegen voor eigenschap Ordentelijke interne bekabeling"""
        return self._ordentelijkeInterneBekabeling.waarde

    @ordentelijkeInterneBekabeling.setter
    def ordentelijkeInterneBekabeling(self, value):
        self._ordentelijkeInterneBekabeling.set_waarde(value, owner=self)

    @property
    def overspanningsbeveiligingInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Overspanningsbeveiliging in orde"""
        return self._overspanningsbeveiligingInOrde.waarde

    @overspanningsbeveiligingInOrde.setter
    def overspanningsbeveiligingInOrde(self, value):
        self._overspanningsbeveiligingInOrde.set_waarde(value, owner=self)

    @property
    def rssBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap RSS buiten gebruik"""
        return self._rssBuitenGebruik.waarde

    @rssBuitenGebruik.setter
    def rssBuitenGebruik(self, value):
        self._rssBuitenGebruik.set_waarde(value, owner=self)

    @property
    def reinigenBordNoodzakelijkFoto(self):
        """Definitie nog toe te voegen voor eigenschap Reinigen bord noodzakelijk (foto)"""
        return self._reinigenBordNoodzakelijkFoto.waarde

    @reinigenBordNoodzakelijkFoto.setter
    def reinigenBordNoodzakelijkFoto(self, value):
        self._reinigenBordNoodzakelijkFoto.set_waarde(value, owner=self)

    @property
    def verlichtingInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Verlichting in orde"""
        return self._verlichtingInOrde.waarde

    @verlichtingInOrde.setter
    def verlichtingInOrde(self, value):
        self._verlichtingInOrde.set_waarde(value, owner=self)

    @property
    def vervangenLuchtfilterS(self):
        """Definitie nog toe te voegen voor eigenschap Vervangen luchtfilter(s)"""
        return self._vervangenLuchtfilterS.waarde

    @vervangenLuchtfilterS.setter
    def vervangenLuchtfilterS(self, value):
        self._vervangenLuchtfilterS.set_waarde(value, owner=self)

    @property
    def verwarmingEnVerluchtingInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Verwarming en verluchting in orde"""
        return self._verwarmingEnVerluchtingInOrde.waarde

    @verwarmingEnVerluchtingInOrde.setter
    def verwarmingEnVerluchtingInOrde(self, value):
        self._verwarmingEnVerluchtingInOrde.set_waarde(value, owner=self)

    @property
    def waterdichtheidBordInOrde(self):
        """Definitie nog toe te voegen voor eigenschap Waterdichtheid bord in orde"""
        return self._waterdichtheidBordInOrde.waarde

    @waterdichtheidBordInOrde.setter
    def waterdichtheidBordInOrde(self, value):
        self._waterdichtheidBordInOrde.set_waarde(value, owner=self)

    @property
    def werkingDiffGetestViaTestknop(self):
        """Definitie nog toe te voegen voor eigenschap Werking diff getest (via testknop)"""
        return self._werkingDiffGetestViaTestknop.waarde

    @werkingDiffGetestViaTestknop.setter
    def werkingDiffGetestViaTestknop(self, value):
        self._werkingDiffGetestViaTestknop.set_waarde(value, owner=self)

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

    @property
    def toestandRssBord(self):
        """Definitie nog toe te voegen voor eigenschap toestand RSS bord"""
        return self._toestandRssBord.waarde

    @toestandRssBord.setter
    def toestandRssBord(self, value):
        self._toestandRssBord.set_waarde(value, owner=self)

