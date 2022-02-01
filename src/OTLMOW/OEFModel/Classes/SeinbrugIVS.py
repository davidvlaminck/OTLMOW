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

        self._aanwezigheidExtraVerhoog = EMAttribuut(field=StringField,
                                                     naam='aanwezigheid extra verhoog',
                                                     label='aanwezigheid extra verhoog',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.aanwezigheidExtraVerhoog',
                                                     definitie='Definitie nog toe te voegen voor eigenschap aanwezigheid extra verhoog')

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

        self._geschilderdSeinbrgivs = EMAttribuut(field=BooleanField,
                                                  naam='geschilderd (SEINBRGIVS)',
                                                  label='geschilderd (SEINBRGIVS)',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.geschilderdSeinbrgivs',
                                                  definitie='corrosiebescherming geschilderd of niet?')

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

        self._opmerkingInventarisSeinbrugIvs = EMAttribuut(field=StringField,
                                                           naam='opmerking inventaris seinbrug IVS',
                                                           label='opmerking inventaris seinbrug IVS',
                                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.opmerkingInventarisSeinbrugIvs',
                                                           definitie='veld waar met max 40 lettertekens aanvullende info kan geleverd worden')

        self._redenSeinbrugIvsBuitenGebruik = EMAttribuut(field=StringField,
                                                          naam='reden seinbrug IVS buiten gebruik',
                                                          label='reden seinbrug IVS buiten gebruik',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugIVS.redenSeinbrugIvsBuitenGebruik',
                                                          definitie='Definitie nog toe te voegen voor eigenschap reden seinbrug IVS buiten gebruik')

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
    def aanwezigheidExtraVerhoog(self):
        """Definitie nog toe te voegen voor eigenschap aanwezigheid extra verhoog"""
        return self._aanwezigheidExtraVerhoog.waarde

    @aanwezigheidExtraVerhoog.setter
    def aanwezigheidExtraVerhoog(self, value):
        self._aanwezigheidExtraVerhoog.set_waarde(value, owner=self)

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
    def geschilderdSeinbrgivs(self):
        """corrosiebescherming geschilderd of niet?"""
        return self._geschilderdSeinbrgivs.waarde

    @geschilderdSeinbrgivs.setter
    def geschilderdSeinbrgivs(self, value):
        self._geschilderdSeinbrgivs.set_waarde(value, owner=self)

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
    def opmerkingInventarisSeinbrugIvs(self):
        """veld waar met max 40 lettertekens aanvullende info kan geleverd worden"""
        return self._opmerkingInventarisSeinbrugIvs.waarde

    @opmerkingInventarisSeinbrugIvs.setter
    def opmerkingInventarisSeinbrugIvs(self, value):
        self._opmerkingInventarisSeinbrugIvs.set_waarde(value, owner=self)

    @property
    def redenSeinbrugIvsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden seinbrug IVS buiten gebruik"""
        return self._redenSeinbrugIvsBuitenGebruik.waarde

    @redenSeinbrugIvsBuitenGebruik.setter
    def redenSeinbrugIvsBuitenGebruik(self, value):
        self._redenSeinbrugIvsBuitenGebruik.set_waarde(value, owner=self)

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
    def typeSeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type seinbrug"""
        return self._typeSeinbrug.waarde

    @typeSeinbrug.setter
    def typeSeinbrug(self, value):
        self._typeSeinbrug.set_waarde(value, owner=self)

