class DotnotatieHelper:
    separator = '.'
    cardinality_separator = '|'
    cardinality_indicator = '[]'

    @staticmethod
    def get_dotnotatie(attribute):
        dotnotatie = attribute.naam
        if attribute.kardinaliteit_max != '1':
            dotnotatie += DotnotatieHelper.cardinality_indicator

        if attribute.owner._parent is not None:
            return attribute.owner._parent.dotnotatie + DotnotatieHelper.separator + dotnotatie

        return dotnotatie

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
            if attribute.field.waardeObject is not None and not attribute.field.waarde_shortcut_applicable:
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
        if attribuut.field.waardeObject is not None and not attribuut.field.waarde_shortcut_applicable:
            field = attribuut.waarde._waarde.field

        return field.convert_to_correct_type(waarde)

    def flatten_dict(self, input_dict:dict, seperator:str = '.', prefix='', affix='', new_dict=None):
        if new_dict is None:
            new_dict = {}
        for k, v in input_dict.items():
            if isinstance(v, dict):
                self.flatten_dict(input_dict=v, prefix=k, new_dict=new_dict)
            elif isinstance(v, list):
                for i in range(0, len(v)):
                    if isinstance(v[i], dict):
                        self.flatten_dict(input_dict=v[i], prefix=k, affix='[' + str(i) + ']', new_dict=new_dict)
                    else:
                        if prefix != '':
                            new_dict[prefix + seperator + k + '[' + str(i) + ']'] = v[i]
                        else:
                            new_dict[k + '[' + str(i) + ']'] = v[i]
            else:
                if prefix != '':
                    new_dict[prefix + affix + seperator + k] = v
                else:
                    new_dict[k] = v

        return new_dict
