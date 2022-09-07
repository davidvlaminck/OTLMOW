# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitspaal(AIMNaamObject, PuntGeometrie):
    """Buiteninstallatie waarin een flitscamera geplaatst kan worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                               naam='externeReferentie',
                                               label='externe referentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal.externeReferentie',
                                               definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...',
                                               owner=self)

    @property
    def externeReferentie(self):
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.get_waarde()

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)
