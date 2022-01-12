# coding=utf-8
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcContactinfo import DtcContactinfo
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBetrokkenheidRol import KlBetrokkenheidRol


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftBetrokkene(DirectioneleRelatie):
    """Koppelt een natuurlijk persoon,rechtspersoon of een hoedanigheid (een functie eerder dan de persoon die de functie uitoefent) aan een object in een bepaalde rol."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.datumAanvang = DateField(naam="datumAanvang",
                                      label="datum aanvang",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.datumAanvang",
                                      definition="De datum waarop de betrokkenheid effectief geworden is of zal worden. ",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De datum waarop de betrokkenheid effectief geworden is of zal worden. """

        self.datumEinde = DateField(naam="datumEinde",
                                    label="datum einde",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.datumEinde",
                                    definition="De datum waarop de betrokkenheid beëindigd is of moet beëindigd worden. ",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De datum waarop de betrokkenheid beëindigd is of moet beëindigd worden. """

        self.rol = KeuzelijstField(naam="rol",
                                   label="rol",
                                   lijst=KlBetrokkenheidRol(),
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.rol",
                                   definition="Type voor de manier waarop een agent betrokken is bij een object.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """Type voor de manier waarop een agent betrokken is bij een object."""

        specifiekeContactinfoField = DtcContactinfo()
        specifiekeContactinfoField.naam = "specifiekeContactinfo"
        specifiekeContactinfoField.label = "specifieke contactinfo"
        specifiekeContactinfoField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.specifiekeContactinfo"
        specifiekeContactinfoField.definition = "Specifieke contactgegevens van de betrokken agent met betrekking tot het gekoppelde object."
        specifiekeContactinfoField.constraints = ""
        specifiekeContactinfoField.usagenote = ""
        specifiekeContactinfoField.deprecated_version = ""
        self.specifiekeContactinfo = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=specifiekeContactinfoField)
        """Specifieke contactgegevens van de betrokken agent met betrekking tot het gekoppelde object."""
