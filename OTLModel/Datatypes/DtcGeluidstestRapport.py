# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KlGCMeetMethode import KlGCMeetMethode
from OTLModel.Datatypes.KlLEGCNorm import KlLEGCNorm
from OTLModel.Datatypes.KlLEGCTestType import KlLEGCTestType


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeluidstestRapportWaarden(AttributeInfo):
    def __init__(self):
        self._geluidsabsorptieReflectie = OTLAttribuut(field=IntegerField,
                                                       naam='geluidsabsorptieReflectie',
                                                       label='geluidsabsorptie reflectie',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.geluidsabsorptieReflectie',
                                                       definition='De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal.')

        self._gemetenWaarde = OTLAttribuut(field=IntegerField,
                                           naam='gemetenWaarde',
                                           label='gemeten waarde',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.gemetenWaarde',
                                           definition='De sterkte van het geluid in dB.')

        self._locatieInSitulabo = OTLAttribuut(field=KlGCMeetMethode,
                                               naam='locatieInSitulabo',
                                               label='locatie in situlabo',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.locatieInSitulabo',
                                               definition='Locatie waar de geluidstest is uitgevoerd (terrein of labo).')

        self._luchtgeluidsisolatie = OTLAttribuut(field=IntegerField,
                                                  naam='luchtgeluidsisolatie',
                                                  label='luchtgeluidsisolatie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.luchtgeluidsisolatie',
                                                  definition='De gemeten waarde van het  luchtgeluidsisiolatie van het geluidsscherm.')

        self._norm = OTLAttribuut(field=KlLEGCNorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.norm',
                                  definition='De proef volgens de beschreven standaard.')

        self._testrapport = OTLAttribuut(field=DtcDocument,
                                         naam='testrapport',
                                         label='testrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.testrapport',
                                         usagenote='Bestanden van het type xlsx of pdf.',
                                         kardinaliteit_max='*',
                                         definition='Documentbijlage met de resultaten van de test.')

        self._type = OTLAttribuut(field=KlLEGCTestType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.type',
                                  definition='Het type van de test.')

    @property
    def geluidsabsorptieReflectie(self):
        """De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal."""
        return self._geluidsabsorptieReflectie.waarde

    @geluidsabsorptieReflectie.setter
    def geluidsabsorptieReflectie(self, value):
        self._geluidsabsorptieReflectie.set_waarde(value)

    @property
    def gemetenWaarde(self):
        """De sterkte van het geluid in dB."""
        return self._gemetenWaarde.waarde

    @gemetenWaarde.setter
    def gemetenWaarde(self, value):
        self._gemetenWaarde.set_waarde(value)

    @property
    def locatieInSitulabo(self):
        """Locatie waar de geluidstest is uitgevoerd (terrein of labo)."""
        return self._locatieInSitulabo.waarde

    @locatieInSitulabo.setter
    def locatieInSitulabo(self, value):
        self._locatieInSitulabo.set_waarde(value)

    @property
    def luchtgeluidsisolatie(self):
        """De gemeten waarde van het  luchtgeluidsisiolatie van het geluidsscherm."""
        return self._luchtgeluidsisolatie.waarde

    @luchtgeluidsisolatie.setter
    def luchtgeluidsisolatie(self, value):
        self._luchtgeluidsisolatie.set_waarde(value)

    @property
    def norm(self):
        """De proef volgens de beschreven standaard."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value)

    @property
    def testrapport(self):
        """Documentbijlage met de resultaten van de test."""
        return self._testrapport.waarde

    @testrapport.setter
    def testrapport(self, value):
        self._testrapport.set_waarde(value)

    @property
    def type(self):
        """Het type van de test."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeluidstestRapport(ComplexField, AttributeInfo):
    """Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft."""
    naam = 'DtcGeluidstestRapport'
    label = 'Geluidstest rapport'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport'
    definition = 'Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft.'
    waardeObject = DtcGeluidstestRapportWaarden

    def __str__(self):
        return ComplexField.__str__(self)

