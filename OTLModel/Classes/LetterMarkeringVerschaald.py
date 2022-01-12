# coding=utf-8
from OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLetterVerschaald import KlLetterVerschaald
from OTLModel.Datatypes.KlLetterVerschaaldType import KlLetterVerschaaldType
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LetterMarkeringVerschaald(FiguratieMarkeringToegang):
    """Een markering bestaande uit letters die een verschaling ondergaat zoals een vergroting en/of een verkleining."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.basisOppervlakte = KwantWrdInVierkanteMeter()
        """De basisoppervlakte van de individuele lettermarkering voor verschaling zoals beschreven in de algemene omzendbrief."""
        self.basisOppervlakte.naam = "basisOppervlakte"
        self.basisOppervlakte.label = "basisoppervlakte"
        self.basisOppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.basisOppervlakte"
        self.basisOppervlakte.definition = "De basisoppervlakte van de individuele lettermarkering voor verschaling zoals beschreven in de algemene omzendbrief."
        self.basisOppervlakte.constraints = ""
        self.basisOppervlakte.usagenote = ""
        self.basisOppervlakte.deprecated_version = ""

        self.letter = KeuzelijstField(naam="letter",
                                      label="letter",
                                      lijst=KlLetterVerschaald(),
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.letter",
                                      definition="De individuele letter gebruikt bij de verschaalde wegmarkering.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De individuele letter gebruikt bij de verschaalde wegmarkering."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van een figuratiemarkering na de verschaling."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van een figuratiemarkering na de verschaling."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLetterVerschaaldType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.type",
                                    definition="Het type van de individuele verschaalde lettermarkering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de individuele verschaalde lettermarkering."""

        self.vergrotingsfactor = DecimalFloatField(naam="vergrotingsfactor",
                                                   label="vergrotingsfactor",
                                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.vergrotingsfactor",
                                                   definition="Een decimaal getal dat weergeeft in welke mate de figuratiemarkering vergroot of verkleind wordt.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Een decimaal getal dat weergeeft in welke mate de figuratiemarkering vergroot of verkleind wordt."""

        self.verlengingsfactor = DecimalFloatField(naam="verlengingsfactor",
                                                   label="verlengingsfactor",
                                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.verlengingsfactor",
                                                   definition="Een decimaal getal dat de verlenging van een figuratiemarkering weergeeft.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Een decimaal getal dat de verlenging van een figuratiemarkering weergeeft."""
