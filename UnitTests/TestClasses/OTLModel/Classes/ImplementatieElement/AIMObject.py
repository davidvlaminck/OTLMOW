# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMToestand import AIMToestand
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from UnitTests.TestClasses.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from UnitTests.TestClasses.OTLModel.Datatypes.KwantWrdInMaand import KwantWrdInMaand
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMObject(AIMDBStatus, AIMToestand, AttributeInfo, OTLAsset, RelatieInteractor):
    """Abstracte als de basisklasse voor alle uniek geïdentificeerde OTL objecten met de basiseigenschappen die elk OTL object minstens heeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AIMToestand.__init__(self)
        AttributeInfo.__init__(self)
        OTLAsset.__init__(self)
        RelatieInteractor.__init__(self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._bestekPostNummer = OTLAttribuut(field=StringField,
                                              naam='bestekPostNummer',
                                              label='bestekpostnummer',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.bestekPostNummer',
                                              kardinaliteit_max='*',
                                              definition='Een verwijzing naar een postnummer uit het specifieke bestek waar het object mee verband houdt.',
                                              owner=self)

        self._datumOprichtingObject = OTLAttribuut(field=DateField,
                                                   naam='datumOprichtingObject',
                                                   label='datum oprichting object',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.datumOprichtingObject',
                                                   definition='Datum van de oprichting van het object.',
                                                   owner=self)

        self._notitie = OTLAttribuut(field=StringField,
                                     naam='notitie',
                                     label='notitie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie',
                                     definition='Extra notitie voor het object.',
                                     owner=self)

        self._standaardBestekPostNummer = OTLAttribuut(field=StringField,
                                                       naam='standaardBestekPostNummer',
                                                       label='standaardbestekpostnummer',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.standaardBestekPostNummer',
                                                       kardinaliteit_max='*',
                                                       definition='Een verwijzing naar een postnummer uit het standaardbestek waar het object mee verband houdt. De notatie van het postnummer moet overeenkomen met de notatie die gebruikt is in de catalogi van standaardbestekken, bijvoorbeeld postnummer 0701.20404G.',
                                                       owner=self)

        self._theoretischeLevensduur = OTLAttribuut(field=KwantWrdInMaand,
                                                    naam='theoretischeLevensduur',
                                                    label='theoretische levensduur',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.theoretischeLevensduur',
                                                    definition=' De levensduur in aantal maanden die theoretisch mag verwacht worden voor een object.',
                                                    owner=self)

    @property
    def assetId(self):
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bestekPostNummer(self):
        """Een verwijzing naar een postnummer uit het specifieke bestek waar het object mee verband houdt."""
        return self._bestekPostNummer.get_waarde()

    @bestekPostNummer.setter
    def bestekPostNummer(self, value):
        self._bestekPostNummer.set_waarde(value, owner=self)

    @property
    def datumOprichtingObject(self):
        """Datum van de oprichting van het object."""
        return self._datumOprichtingObject.get_waarde()

    @datumOprichtingObject.setter
    def datumOprichtingObject(self, value):
        self._datumOprichtingObject.set_waarde(value, owner=self)

    @property
    def notitie(self):
        """Extra notitie voor het object."""
        return self._notitie.get_waarde()

    @notitie.setter
    def notitie(self, value):
        self._notitie.set_waarde(value, owner=self)

    @property
    def standaardBestekPostNummer(self):
        """Een verwijzing naar een postnummer uit het standaardbestek waar het object mee verband houdt. De notatie van het postnummer moet overeenkomen met de notatie die gebruikt is in de catalogi van standaardbestekken, bijvoorbeeld postnummer 0701.20404G."""
        return self._standaardBestekPostNummer.get_waarde()

    @standaardBestekPostNummer.setter
    def standaardBestekPostNummer(self, value):
        self._standaardBestekPostNummer.set_waarde(value, owner=self)

    @property
    def theoretischeLevensduur(self):
        """ De levensduur in aantal maanden die theoretisch mag verwacht worden voor een object."""
        return self._theoretischeLevensduur.get_waarde()

    @theoretischeLevensduur.setter
    def theoretischeLevensduur(self, value):
        self._theoretischeLevensduur.set_waarde(value, owner=self)
