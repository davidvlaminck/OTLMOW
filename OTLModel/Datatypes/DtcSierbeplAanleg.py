# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAanplantingswijzeSierbeplanting import KlAanplantingswijzeSierbeplanting
from OTLModel.Datatypes.KlSierbeplContainer import KlSierbeplContainer
from OTLModel.Datatypes.KlSierbeplPlantmaat import KlSierbeplPlantmaat
from OTLModel.Datatypes.KlVegetatiePlantverband import KlVegetatiePlantverband
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSierbeplAanleg(ComplexField):
    """Complex datatype voor dat de aanleg van sierbeplanting beschrijft."""

    def __init__(self):
        super().__init__(naam="DtcSierbeplAanleg",
                         label="Sierbeplanting aanleg",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg",
                         definition="Complex datatype voor dat de aanleg van sierbeplanting beschrijft.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.aanplantingswijze = KeuzelijstField(naam="aanplantingswijze",
                                                        label="aanplantingswijze",
                                                        lijst=KlAanplantingswijzeSierbeplanting(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.aanplantingswijze",
                                                        definition="Manier van aanplanten.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.aanplantingswijze = self.waarde.aanplantingswijze
        """Manier van aanplanten."""

        self.waarde.containermaat = KeuzelijstField(naam="containermaat",
                                                    label="containermaat",
                                                    lijst=KlSierbeplContainer(),
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.containermaat",
                                                    definition="De grootte van de pot of container waarin de plant wordt geleverd. De P staat voor pot, de C voor container. Het getal geeft de grootte weer in centimeter.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        self.containermaat = self.waarde.containermaat
        """De grootte van de pot of container waarin de plant wordt geleverd. De P staat voor pot, de C voor container. Het getal geeft de grootte weer in centimeter."""

        self.waarde.plantdichtheid = NonNegIntegerField(naam="plantdichtheid",
                                                        label="plantdichtheid",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantdichtheid",
                                                        definition="Aantal planten per vierkante meter.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.plantdichtheid = self.waarde.plantdichtheid
        """Aantal planten per vierkante meter."""

        self.waarde.plantmaat = KeuzelijstField(naam="plantmaat",
                                                label="plantmaat",
                                                lijst=KlSierbeplPlantmaat(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantmaat",
                                                definition="De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.plantmaat = self.waarde.plantmaat
        """De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde."""

        self.waarde.plantverband = KeuzelijstField(naam="plantverband",
                                                   label="plantverband",
                                                   lijst=KlVegetatiePlantverband(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantverband",
                                                   definition="De wijze waarop de planten zijn geschikt.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        self.plantverband = self.waarde.plantverband
        """De wijze waarop de planten zijn geschikt."""
