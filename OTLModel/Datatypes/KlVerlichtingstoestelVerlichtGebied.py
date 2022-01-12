# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelVerlichtGebied(Keuzelijst):
    """Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel."""

    def __init__(self):
        super().__init__(naam="KlVerlichtingstoestelVerlichtGebied",
                         label="Verlichtingstoestel verlicht gebied.",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelVerlichtGebied",
                         definition="Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelVerlichtGebied")

        self.add_option("afrit", "afrit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/afrit")
        self.add_option("bebakening", "bebakening", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/bebakening")
        self.add_option("doorlopende-straatverlichting", "doorlopende straatverlichting", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/doorlopende-straatverlichting")
        self.add_option("fietspad", "fietspad", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/fietspad")
        self.add_option("hoofdweg", "hoofdweg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/hoofdweg")
        self.add_option("kruispunt", "kruispunt", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/kruispunt")
        self.add_option("monument", "monument", "Alle niet-functie verlichting, dus alle verlichting die nodig is om je weg te vinden.Verlichting voor artistieke creaties op (bv. rotonde) of rond de openbare weg (bv. ecoduct dat onderaan een schilderij heeft) of voor artistieke belichting (niet verlichting) te geven, bv een hangbrug waarbij de kabels aangelicht worden. Somskan dit ook zijn voor het aanlichten of belichten van gebouwen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/monument")
        self.add_option("onderdoorgang", "onderdoorgang", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/onderdoorgang")
        self.add_option("oprit", "oprit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/oprit")
        self.add_option("parking", "parking", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/parking")
        self.add_option("projector", "projector", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/projector")
        self.add_option("punctuele-verlichting", "punctuele verlichting", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/punctuele-verlichting")
        self.add_option("rotonde", "rotonde", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/rotonde")
        self.add_option("tunnelverlichting", "tunnelverlichting", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/tunnelverlichting")
        self.add_option("wisselaar", "wisselaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/wisselaar")
