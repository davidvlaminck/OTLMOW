# coding=utf-8
from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie


class GeldigeRelatieLijst:
    def __init__(self):
        self.lijst = [
            GeldigeRelatie("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging", ""),
            GeldigeRelatie("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt", "")
        ]
