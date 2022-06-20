# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.SoftwareToegang import SoftwareToegang
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcSoftwarePoortconfiguratie import DtcSoftwarePoortconfiguratie
from OTLMOW.OTLModel.Datatypes.KlSoftwareLicentie import KlSoftwareLicentie
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.URIField import URIField
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Software(SoftwareToegang, GeenGeometrie):
    """Geheel van computerprogramma's met bijbehorende data."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        SoftwareToegang.__init__(self)
        GeenGeometrie.__init__(self)

        self._aangebodenServices = OTLAttribuut(field=DtcDocument,
                                                naam='aangebodenServices',
                                                label='aangeboden services',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.aangebodenServices',
                                                definition='De endpoints van diensten.',
                                                owner=self)

        self._buildnummer = OTLAttribuut(field=StringField,
                                         naam='buildnummer',
                                         label='buildnummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.buildnummer',
                                         definition='De software build.',
                                         owner=self)

        self._dependencies = OTLAttribuut(field=DtcDocument,
                                          naam='dependencies',
                                          label='dependencies',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.dependencies',
                                          definition='Afhankelijkheden met andere diensten.',
                                          owner=self)

        self._documentatie = OTLAttribuut(field=StringField,
                                          naam='documentatie',
                                          label='documentatie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.documentatie',
                                          usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                          deprecated_version='2.1.0',
                                          definition='Link naar documentatie over de software.',
                                          owner=self)

        self._licentie = OTLAttribuut(field=KlSoftwareLicentie,
                                      naam='licentie',
                                      label='licentie',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.licentie',
                                      definition='De licentievorm van de software (bv. commercieel, shareware, freeware, open source [BSD, Apache, GPL],...).',
                                      owner=self)

        self._onlineDocumentatie = OTLAttribuut(field=URIField,
                                                naam='onlineDocumentatie',
                                                label='online documentatie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.onlineDocumentatie',
                                                definition='De url waarop documentatie over de software te vinden is.',
                                                owner=self)

        self._poortenconfiguratie = OTLAttribuut(field=DtcSoftwarePoortconfiguratie,
                                                 naam='poortenconfiguratie',
                                                 label='poortenconfiguratie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.poortenconfiguratie',
                                                 kardinaliteit_max='*',
                                                 definition='Beschrijft welke poort voor welke service gebruikt wordt.',
                                                 owner=self)

        self._versie = OTLAttribuut(field=StringField,
                                    naam='versie',
                                    label='versie',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.versie',
                                    definition='Het versienummer van de software.',
                                    owner=self)

    @property
    def aangebodenServices(self):
        """De endpoints van diensten."""
        return self._aangebodenServices.get_waarde()

    @aangebodenServices.setter
    def aangebodenServices(self, value):
        self._aangebodenServices.set_waarde(value, owner=self)

    @property
    def buildnummer(self):
        """De software build."""
        return self._buildnummer.get_waarde()

    @buildnummer.setter
    def buildnummer(self, value):
        self._buildnummer.set_waarde(value, owner=self)

    @property
    def dependencies(self):
        """Afhankelijkheden met andere diensten."""
        return self._dependencies.get_waarde()

    @dependencies.setter
    def dependencies(self, value):
        self._dependencies.set_waarde(value, owner=self)

    @property
    def documentatie(self):
        """Link naar documentatie over de software."""
        return self._documentatie.get_waarde()

    @documentatie.setter
    def documentatie(self, value):
        self._documentatie.set_waarde(value, owner=self)

    @property
    def licentie(self):
        """De licentievorm van de software (bv. commercieel, shareware, freeware, open source [BSD, Apache, GPL],...)."""
        return self._licentie.get_waarde()

    @licentie.setter
    def licentie(self, value):
        self._licentie.set_waarde(value, owner=self)

    @property
    def onlineDocumentatie(self):
        """De url waarop documentatie over de software te vinden is."""
        return self._onlineDocumentatie.get_waarde()

    @onlineDocumentatie.setter
    def onlineDocumentatie(self, value):
        self._onlineDocumentatie.set_waarde(value, owner=self)

    @property
    def poortenconfiguratie(self):
        """Beschrijft welke poort voor welke service gebruikt wordt."""
        return self._poortenconfiguratie.get_waarde()

    @poortenconfiguratie.setter
    def poortenconfiguratie(self, value):
        self._poortenconfiguratie.set_waarde(value, owner=self)

    @property
    def versie(self):
        """Het versienummer van de software."""
        return self._versie.get_waarde()

    @versie.setter
    def versie(self, value):
        self._versie.set_waarde(value, owner=self)
