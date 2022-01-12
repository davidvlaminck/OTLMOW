# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringSoort(Keuzelijst):
    """De soorten van markingsproduct. Afgeleid van de COPRO_code."""

    def __init__(self):
        super().__init__(naam="KlMarkeringSoort",
                         label="Soort markeringsproduct",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMarkeringSoort",
                         definition="De soorten van markingsproduct. Afgeleid van de COPRO_code.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringSoort")

        self.add_option("geprefabriceerd", "geprefabriceerd", "Voorgevormde wegmarkering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/geprefabriceerd")
        self.add_option("koudplastisch", "koudplastisch", "Een koudplast is een markeringssubstantie gevormd door de chemische reactie van 2 of meerdere componenten (minstens 1 verharder en 1 hoofdcomponent), waarvan geen oplosmiddelen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/koudplastisch")
        self.add_option("thermoplastisch-vlak", "thermoplastisch vlak", "Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Een vlak systeem is een film met constante dosering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastisch-vlak")
        self.add_option("thermoplastische-multi-dot", "thermoplastische multi-dot", "Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Geprofileerde systemen hebben in dwars- en of lengterichting veranderlijke filmdikte. Hierdoor ontstaat een reliëf met een wisselende hoogte.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastische-multi-dot")
        self.add_option("thermoplastische-ribbelmarkering", "thermoplastische ribbelmarkering", "Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Geprofileerde systemen hebben in dwars- en of lengterichting veranderlijke filmdikte. Hierdoor ontstaat een reliëf met een wisselende hoogte.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastische-ribbelmarkering")
        self.add_option("verf", "verf", "Wegenverf die zich uitstekend leent tot de markering van openbare wegen. Wegenverf is een vloeibaar product dat vaste stoffen zoals bindmiddel, stoffen die kleuren reflecteren, vulstoffen en additieven bevat.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/verf")
