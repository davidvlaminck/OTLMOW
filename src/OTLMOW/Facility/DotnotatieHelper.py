class DotnotatieHelper:
    separator = '.'
    cardinality_separator = '|'
    cardinality_indicator = '[]'
    waarde_shortcut_applicable = False

    @staticmethod
    def set_parameters_to_class_vars(cardinality_indicator, separator, waarde_shortcut_applicable):
        if separator == '':
            separator = DotnotatieHelper.separator
        if cardinality_indicator == '':
            cardinality_indicator = DotnotatieHelper.cardinality_indicator
        if waarde_shortcut_applicable is None:
            waarde_shortcut_applicable = DotnotatieHelper.waarde_shortcut_applicable
        return cardinality_indicator, separator, waarde_shortcut_applicable

    @staticmethod
    def get_dotnotatie(attribute, separator: str = '', cardinality_indicator: str = '',
                       waarde_shortcut_applicable: bool | None = None):
        cardinality_indicator, separator, waarde_shortcut_applicable = DotnotatieHelper.set_parameters_to_class_vars(
            cardinality_indicator, separator, waarde_shortcut_applicable)

        if waarde_shortcut_applicable:
            if attribute.naam == 'waarde' and attribute.owner._parent is not None and attribute.owner._parent.field.waarde_shortcut_applicable:
                return attribute.owner._parent.dotnotatie

        dotnotatie = attribute.naam
        if attribute.kardinaliteit_max != '1':
            dotnotatie += cardinality_indicator

        if attribute.owner._parent is not None:
            return attribute.owner._parent.dotnotatie + separator + dotnotatie

        return dotnotatie

    @staticmethod
    def get_attributes_by_dotnotatie(instanceOrAttribute, dotnotatie, separator: str = '', cardinality_indicator: str = '',
                                     waarde_shortcut_applicable: bool | None = None):
        cardinality_indicator, separator, waarde_shortcut_applicable = DotnotatieHelper.set_parameters_to_class_vars(
            cardinality_indicator, separator, waarde_shortcut_applicable)

        if waarde_shortcut_applicable and separator not in dotnotatie:
            attribute = getattr(instanceOrAttribute, '_' + dotnotatie.replace(cardinality_indicator, ''))
            if attribute.field.waarde_shortcut_applicable:
                waardenObject = getattr(instanceOrAttribute, dotnotatie.replace(cardinality_indicator, ''))
                if cardinality_indicator in dotnotatie:
                    collect_attributes = []
                    for waardenObject_in_list in waardenObject:
                        collect_attributes.append(getattr(waardenObject_in_list, '_waarde'))
                    return collect_attributes
                else:
                    return getattr(waardenObject, '_waarde')

        if separator in dotnotatie:
            first = dotnotatie.split(separator)[0]
            rest = dotnotatie.split(separator, 1)[1]
            if cardinality_indicator in first:
                first = first.replace(cardinality_indicator, '')
                attribute = getattr(instanceOrAttribute, first)
                collect_attributes = []
                for attr_in_list in attribute:
                    collect_attributes.append(DotnotatieHelper.get_attributes_by_dotnotatie(attr_in_list, rest))
                return collect_attributes
            else:
                attribute = getattr(instanceOrAttribute, first)
                return DotnotatieHelper.get_attributes_by_dotnotatie(attribute, rest)
        else:
            if cardinality_indicator in dotnotatie:
                return getattr(instanceOrAttribute, '_' + dotnotatie.replace(cardinality_indicator, ''))
            else:
                return getattr(instanceOrAttribute, '_' + dotnotatie)

    # TODO add shortcut waarde option
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
    def convert_waarde_to_correct_type(waarde, attribuut):
        field = attribuut.field
        if attribuut.field.waardeObject is not None and not attribuut.field.waarde_shortcut_applicable:
            field = attribuut.waarde._waarde.field

        return field.convert_to_correct_type(waarde)

    def flatten_dict(self, input_dict: dict, seperator: str = '.', prefix='', affix='', new_dict=None):
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
