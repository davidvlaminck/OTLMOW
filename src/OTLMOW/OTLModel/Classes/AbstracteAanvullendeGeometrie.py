# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.Classes.AIMToestand import AIMToestand
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AbstracteAanvullendeGeometrie(AIMDBStatus, AIMToestand):
    """Abstracte om de eigenschappen en relaties van AanvullendeGeometrie te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AIMToestand.__init__(self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.assetId',
                                     definition='Unieke identificatie van de aanvullende geometrie zoals toegekend door de beheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._bijlage = OTLAttribuut(field=DtcDocument,
                                     naam='bijlage',
                                     label='bijlage',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.bijlage',
                                     definition='Het document of artefact dat een geometrie heeft.',
                                     owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.naam',
                                  definition='De mensleesbare naam van een aanvullende geometrie. De beheerder kent deze naam toe of geeft de opdracht om deze toe te kennen.',
                                  owner=self)

        self._typeUri = OTLAttribuut(field=URIField,
                                     naam='typeUri',
                                     label='type URI',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.typeUri',
                                     definition='De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI .',
                                     owner=self)

    @property
    def assetId(self):
        """Unieke identificatie van de aanvullende geometrie zoals toegekend door de beheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.waarde

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bijlage(self):
        """Het document of artefact dat een geometrie heeft."""
        return self._bijlage.waarde

    @bijlage.setter
    def bijlage(self, value):
        self._bijlage.set_waarde(value, owner=self)

    @property
    def naam(self):
        """De mensleesbare naam van een aanvullende geometrie. De beheerder kent deze naam toe of geeft de opdracht om deze toe te kennen."""
        return self._naam.waarde

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def typeUri(self):
        """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI ."""
        return self._typeUri.waarde

    @typeUri.setter
    def typeUri(self, value):
        self._typeUri.set_waarde(value, owner=self)
