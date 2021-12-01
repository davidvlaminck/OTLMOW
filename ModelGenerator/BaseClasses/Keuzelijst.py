from abc import ABC

from ModelGenerator.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


class Keuzelijst(ABC):
    def __init__(self, naam, label, uri):
        self.naam = naam
        self.label = label
        self.uri = uri
        self.options = []

    def addOption(self, waarde, label, definitie, uri):
        self.options.append(KeuzelijstWaarde(waarde, label, definitie, uri))