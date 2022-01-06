# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerkeersbordCategorie import KlVerkeersbordCategorie
from OTLModel.Datatypes.KlVerkeersbordCode import KlVerkeersbordCode
from OTLModel.Datatypes.KlVerkeersbordconceptStatus import KlVerkeersbordconceptStatus
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersbordConcept(AIMObject):
    """Inhoudelijke definitie van de betekenis van een verkeersbord zoals opgenomen in de wegcode."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        afbeeldingField = DtcDocument()
        afbeeldingField.naam = "afbeelding"
        afbeeldingField.label = "afbeelding"
        afbeeldingField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.afbeelding"
        afbeeldingField.definition = "De afbeelding van het verkeersbordconcept."
        afbeeldingField.constraints = ""
        afbeeldingField.usagenote = ""
        afbeeldingField.deprecated_version = ""
        self.afbeelding = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=afbeeldingField)
        """De afbeelding van het verkeersbordconcept."""

        self.betekenis = StringField(naam="betekenis",
                                     label="betekenis",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.betekenis",
                                     definition="Betekenis die gegeven wordt aan dit soort verkeersbord volgens de wegcode.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Betekenis die gegeven wordt aan dit soort verkeersbord volgens de wegcode."""

        self.rechtsgrondOnderdeel = DtcExterneReferentie()
        """Verwijst naar een rechtsgrondonderdeel over dit verkeersbordconcept."""
        self.rechtsgrondOnderdeel.naam = "rechtsgrondOnderdeel"
        self.rechtsgrondOnderdeel.label = "rechtsgrondonderdeel"
        self.rechtsgrondOnderdeel.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.rechtsgrondOnderdeel"
        self.rechtsgrondOnderdeel.definition = "Verwijst naar een rechtsgrondonderdeel over dit verkeersbordconcept."
        self.rechtsgrondOnderdeel.constraints = ""
        self.rechtsgrondOnderdeel.usagenote = "Verwijst meestal naar een artikel in de wegcode die informatie over dit verkeersbordconcept bevat. Bijvoorbeeld: artikel 68.3 voor verbodsborden."
        self.rechtsgrondOnderdeel.deprecated_version = ""

        self.status = KeuzelijstField(naam="status",
                                      label="status",
                                      lijst=KlVerkeersbordconceptStatus(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.status",
                                      definition="Duidt of het verkeersbordconcept nog gebruikt wordt.",
                                      constraints="",
                                      usagenote="Bijvoorbeeld: stabiel, onstabiel, afgeschaft. Een bord met snelheidslimiet van 60 km/u is bijvoorbeeld afgeschaft.",
                                      deprecated_version="")
        """Duidt of het verkeersbordconcept nog gebruikt wordt."""

        self.verkeersbordCategorie = KeuzelijstField(naam="verkeersbordCategorie",
                                                     label="verkeersbord categorie",
                                                     lijst=KlVerkeersbordCategorie(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.verkeersbordCategorie",
                                                     definition="Categorie van het verkeersbordconcept.	.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Categorie van het verkeersbordconcept.	."""

        self.verkeersbordCode = KeuzelijstField(naam="verkeersbordCode",
                                                label="verkeersbordcode",
                                                lijst=KlVerkeersbordCode(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.verkeersbordCode",
                                                definition="Code die aan dit soort bord gegeven wordt binnen de wegcode.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Code die aan dit soort bord gegeven wordt binnen de wegcode."""
