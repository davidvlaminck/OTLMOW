# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrazigeVegetatieAanleg(Keuzelijst):
    """Types van aanleg voor de grazige vegetatie."""

    def __init__(self):
        super().__init__(naam="KlGrazigeVegetatieAanleg",
                         label="Grazige vegetatie aanleg",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrazigeVegetatieAanleg",
                         definition="Types van aanleg voor de grazige vegetatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrazigeVegetatieAanleg")

        self.add_option("aanplanting-container-planten", "aanplanting container planten", "Het aanleggen van een grazige vegetatie dmv de aanplant van container planten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/aanplanting-container-planten")
        self.add_option("aanplanting-wortelstokken", "aanplanting wortelstokken", "Het aanleggen van een grazige vegetatie dmv de aanplant van wortelstokken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/aanplanting-wortelstokken")
        self.add_option("bezaaiing", "bezaaiing", "Het aanleggen van een grazige vegetatie door het inzaaien van het zaadmengsel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bezaaiing")
        self.add_option("bezoding", "bezoding", "Het aanleggen van een grazige vegetatie door het naast elkaar leggen van graszoden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bezoding")
        self.add_option("bloemenmengsel", "bloemenmengsel", "Het aanleggen van een grazige vegetatie door het inzaaien van een bloemenmengsel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bloemenmengsel")
        self.add_option("hydraulische-bezaaiing", "hydraulische bezaaiing", "Het aanleggen van een grazige vegetatie door het openspreiden van het zaadmengsel met een spuitzaaimachine.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/hydraulische-bezaaiing")
        self.add_option("natuurlijke-vegetatie-ontwikkeling-door-behoud-zaadbank", "natuurlijke vegetatie ontwikkeling door behoud zaadbank", "Het ontstaan van natuurlijke grazige vegetatie door behoud van de zaadbank.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/natuurlijke-vegetatie-ontwikkeling-door-behoud-zaadbank")
        self.add_option("natuurlijke-vegetatie-ontwikkeling-door-overbrengen-maaisel", "natuurlijke vegetatie ontwikkeling door overbrengen maaisel", "Het ontstaan van natuurlijke grazige vegetatie door overbrengen van maaisel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/natuurlijke-vegetatie-ontwikkeling-door-overbrengen-maaisel")
        self.add_option("rhizomen", "rhizomen", "Het aanleggen van een grazige vegetatie dmv rhizomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/rhizomen")
