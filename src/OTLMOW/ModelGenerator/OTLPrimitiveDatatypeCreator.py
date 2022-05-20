import logging

from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, osloCollector: OSLOCollector):
        super().__init__(osloCollector)
        logging.info("Created an instance of OTLPrimitiveDatatypeCreator")

    def CreateBlockToWriteFromPrimitiveTypes(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        if not isinstance(osloDatatypePrimitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if osloDatatypePrimitive.objectUri == '' or not (osloDatatypePrimitive.objectUri.startswith('http://www.w3.org/200') or
                                                         osloDatatypePrimitive.objectUri.startswith(
                                                             'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                                                         or osloDatatypePrimitive.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(f"OSLODatatypePrimitive.objectUri is invalid. Value = '{osloDatatypePrimitive.objectUri}'")
        if osloDatatypePrimitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{osloDatatypePrimitive.name}'")

        if osloDatatypePrimitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypePrimitive, typeField='KwantWrd')
        if osloDatatypePrimitive.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypePrimitive, typeField='Primitive')
