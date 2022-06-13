# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcAardingsstelsel import DtcAardingsstelsel
from OTLMOW.OTLModel.Datatypes.KlAardingAardingsnet import KlAardingAardingsnet
from OTLMOW.OTLModel.Datatypes.KwantWrdInOhm import KwantWrdInOhm
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingsinstallatie(AIMNaamObject, VlakGeometrie):
    """Een galvanische verbinding van een elektrische installatie met de aarde. De elektrische installatie die op deze wijze met de aarde wordt verbonden krijgt een spanning van nul volt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._aardingsnet = OTLAttribuut(field=KlAardingAardingsnet,
                                         naam='aardingsnet',
                                         label='aardingsnet',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie.aardingsnet',
                                         definition='De manier waarop respectievelijk de bron en de verbruiker met de aarde verbonden worden om op die manier foutstromen af te voeren.',
                                         owner=self)

        self._aardingsstelsel = OTLAttribuut(field=DtcAardingsstelsel,
                                             naam='aardingsstelsel',
                                             label='aardingsstelsel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie.aardingsstelsel',
                                             definition='De wijze waarop verschillende aardingen (bv. laagspanningsaarding, nulpuntsaarding, hoogspanningsaarding) zich t.o.v. elkaar bevinden: ofwel bevinden alle aardingen zich uit elkaars invloedssfeer en hebben ze geen impact op elkaars potentiaal ofwel zijn alle aardverbindingen galvanisch met elkaar in contact. In het eerste geval spreekt men van gescheiden aardingsstelsel, in het tweede geval van een globale aarding.',
                                             owner=self)

        self._aardingsweerstand = OTLAttribuut(field=KwantWrdInOhm,
                                               naam='aardingsweerstand',
                                               label='aardingsweerstand',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie.aardingsweerstand',
                                               definition='De grootte van de weerstand tussen de aardelektrode en de omringende grond.',
                                               owner=self)

    @property
    def aardingsnet(self):
        """De manier waarop respectievelijk de bron en de verbruiker met de aarde verbonden worden om op die manier foutstromen af te voeren."""
        return self._aardingsnet.get_waarde()

    @aardingsnet.setter
    def aardingsnet(self, value):
        self._aardingsnet.set_waarde(value, owner=self)

    @property
    def aardingsstelsel(self):
        """De wijze waarop verschillende aardingen (bv. laagspanningsaarding, nulpuntsaarding, hoogspanningsaarding) zich t.o.v. elkaar bevinden: ofwel bevinden alle aardingen zich uit elkaars invloedssfeer en hebben ze geen impact op elkaars potentiaal ofwel zijn alle aardverbindingen galvanisch met elkaar in contact. In het eerste geval spreekt men van gescheiden aardingsstelsel, in het tweede geval van een globale aarding."""
        return self._aardingsstelsel.get_waarde()

    @aardingsstelsel.setter
    def aardingsstelsel(self, value):
        self._aardingsstelsel.set_waarde(value, owner=self)

    @property
    def aardingsweerstand(self):
        """De grootte van de weerstand tussen de aardelektrode en de omringende grond."""
        return self._aardingsweerstand.get_waarde()

    @aardingsweerstand.setter
    def aardingsweerstand(self, value):
        self._aardingsweerstand.set_waarde(value, owner=self)
