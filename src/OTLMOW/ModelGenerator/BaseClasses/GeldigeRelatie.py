class GeldigeRelatie:
    def __init__(self, bron: str, doel: str, relatie: str, deprecated_version: str):
        self.relatie = relatie
        self.doel = doel
        self.bron = bron
        self.deprecated_version = deprecated_version
