from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBetonmilieuklasse(Keuzelijst):
    """Milieuklasse (X-klasse) waaraan het beton wordt blootgesteld."""

    def __init__(self):
        super().__init__(naam="KlBetonmilieuklasse",
                         label="Betonmilieuklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBetonmilieuklasse",
                         definition="Milieuklasse (X-klasse) waaraan het beton wordt blootgesteld.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonmilieuklasse")

        self.add_option("x-a-1", "XA1", "Chemische aantasting (Aggressive) : zwak agressieve omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-1")
        self.add_option("x-f-3", "XF3", "Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving verzadigd met water, zonder dooizouten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-3")
        self.add_option("x-c-4", "XC4", "Corrosie ingeleid door carbonatatie (Carbonatation) : wisselend natte en droge omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-4")
        self.add_option("x-f-2", "XF2", "Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving niet-volledig verzadigd met water, met dooizouten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-2")
        self.add_option("x-d-3", "XD3", "Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : wisselend natte en droge omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-3")
        self.add_option("x-s-1", "XS1", "Corrosie ingeleid door chloriden (zeewater, Seawater) : omgeving met zouthoudende lucht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-1")
        self.add_option("x-d-2", "XD2", "Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : natte omgeving die zelden droog is.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-2")
        self.add_option("x-s-2", "XS2", "Corrosie ingeleid door chloriden (zeewater, Seawater) : blijvend onder zeewater.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-2")
        self.add_option("x-c-2", "XC2", "Corrosie ingeleid door carbonatatie (Carbonatation) : natte omgeving die zelden droog is.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-2")
        self.add_option("x-c-3", "XC3", "Corrosie ingeleid door carbonatatie (Carbonatation) : omgeving met matige vochtigheid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-3")
        self.add_option("x-s-3", "XS3", "Corrosie ingeleid door chloriden (zeewater, Seawater) : getijde-, spat- en stuifzone.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-3")
        self.add_option("x-a-3", "XA3", "Chemische aantasting (Aggressive) : sterk agressieve omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-3")
        self.add_option("x-c-1", "XC1", "Corrosie ingeleid door carbonatatie (Carbonatation) : droge of blijvend natte omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-1")
        self.add_option("x-d-1", "XD1", "Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : omgeving met matige vochtigheid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-1")
        self.add_option("x-f-4", "XF4", "Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving verzadigd met water, met dooizouten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-4")
        self.add_option("x-f-1", "XF1", "Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving niet-volledig verzadigd met water, zonder dooizouten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-1")
        self.add_option("x-0", "X0", "Geen risico op corrosie of aantasting, voor beton zonder wapening of ingesloten metalen, behalve bij vorst, dooi of chemische aantasting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-0")
        self.add_option("x-a-2", "XA2", "Chemische aantasting (Aggressive) : matig agressieve omgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-2")
