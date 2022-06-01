# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.KlTypeWindverband import KlTypeWindverband


# Generated with OTLClassCreator. To modify: extend, do not edit
class Windverband(ConstructiefObject):
    """Ook: kruisverband. Stabiliteitsvoorziening om een constructie stijf te maken. Vangt windbelastingen, spatkrachten en dwarskrachten op. Ze bestaan meestal uit vrijwel onwrikbare (onvervormbare) driehoeken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Windverband'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlTypeWindverband,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Windverband.type',
                                  definition='Type windverband',
                                  owner=self)

    @property
    def type(self):
        """Type windverband"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
