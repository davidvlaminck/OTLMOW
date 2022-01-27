from OTLMOW.Facility.ComplexFieldSetter import ComplexFieldSetter
from OTLMOW.Facility.PrimitiveFieldSetter import PrimitiveFieldSetter
from OTLMOW.Facility.KeuzelijstFieldSetter import KeuzelijstFieldSetter
from OTLMOW.OTLModel.Datatypes import KeuzelijstField


class AttributeSetterFactory:  # TODO write tests
    @classmethod
    def CreateSetter(cls, instance, attr_naam=None):
        if attr_naam is not None:
            try:
                attribute = getattr(instance, '_' + attr_naam)
            except AttributeError as ex:
                if attr_naam == "bron" or attr_naam == "doel":
                    return None  # TODO decide whether or not to implement bron and doel attributes of relatie
                raise NotImplementedError(str(ex))
        else:
            attribute = instance

        if attribute.field.waardeObject is not None:
            return ComplexFieldSetter(attribute)
        if isinstance(attribute.field(), KeuzelijstField):
            return KeuzelijstFieldSetter(attribute)
        return PrimitiveFieldSetter(attribute)