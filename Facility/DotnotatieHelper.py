from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


class DotnotatieHelper:
    @staticmethod
    def set_attribute_by_dotnotatie(instanceOrAttribute, dotnotatie, value, convert=True):
        if '.' in dotnotatie:
            first = dotnotatie.split('.')[0]
            rest = dotnotatie.split('.', 1)[1]
            attribute = getattr(instanceOrAttribute, first)
            return DotnotatieHelper.set_attribute_by_dotnotatie(attribute, rest, value, convert)
        else:
            attribute = getattr(instanceOrAttribute, '_' + dotnotatie)
            if convert:
                value = DotnotatieHelper.convert_waarde_to_correct_type(value, attribute)
            if attribute.field.waardeObject is not None and not attribute.field._uses_waarde_object:
                setattr(attribute.waarde, 'waarde', value)
            else:
                setattr(instanceOrAttribute, dotnotatie, value)

    @staticmethod
    def get_attribute_by_dotnotatie(instanceOrAttribute, dotnotatie):
        if '.' in dotnotatie:
            first = dotnotatie.split('.')[0]
            rest = dotnotatie.split('.', 1)[1]
            attribute = getattr(instanceOrAttribute, first)
            return DotnotatieHelper.get_attribute_by_dotnotatie(attribute, rest)
        else:
            return getattr(instanceOrAttribute, '_' + dotnotatie)

    @staticmethod
    def convert_waarde_to_correct_type(waarde, attribuut):
        field = attribuut.field
        if attribuut.field.waardeObject is not None and not attribuut.field._uses_waarde_object:
            field = attribuut.waarde._waarde.field

        return field.convert_to_correct_type(waarde)


