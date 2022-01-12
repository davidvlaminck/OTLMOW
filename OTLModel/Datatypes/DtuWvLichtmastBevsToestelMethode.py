# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWvLichtmastBevsToestel import KlWvLichtmastBevsToestel
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuWvLichtmastBevsToestelMethode(UnionTypeField):
    """Union datatype voor de wijze waarop verlichtingstoestellen bevestigd zijn op een lichtmast, indien dit een standaard methode is dan kan deze geselecteerd worden uit een keuzelijst. Bij afwijkende methode kan de methode toegelicht worden."""

    def __init__(self):
        super().__init__(naam="DtuWvLichtmastBevsToestelMethode",
                         label="Bevestiging wegverlichtingstoestel",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode",
                         definition="Union datatype voor de wijze waarop verlichtingstoestellen bevestigd zijn op een lichtmast, indien dit een standaard methode is dan kan deze geselecteerd worden uit een keuzelijst. Bij afwijkende methode kan de methode toegelicht worden.",
                         usagenote="",
                         deprecated_version="")

        field_afwijkendeMethode = StringField(naam="afwijkendeMethode",
                                              label="afwijkende methode",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode.afwijkendeMethode",
                                              definition="Tekstveld waarin de afwijkende methode van bevestiging van verlichtingstoestel aan lichtmast kan beschreven worden.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Tekstveld waarin de afwijkende methode van bevestiging van verlichtingstoestel aan lichtmast kan beschreven worden."""

        field_standaardMethode = KeuzelijstField(naam="standaardMethode",
                                                 label="standaard methode",
                                                 lijst=KlWvLichtmastBevsToestel(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuWvLichtmastBevsToestelMethode.standaardMethode",
                                                 definition="Bepaling van de standaardbevestigingen van verlichtingstoestellen aan lichtmasten.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van de standaardbevestigingen van verlichtingstoestellen aan lichtmasten."""

        self.fieldsTuple = (field_afwijkendeMethode, field_standaardMethode)
