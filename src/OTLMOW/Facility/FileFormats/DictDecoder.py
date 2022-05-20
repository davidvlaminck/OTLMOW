class DictDecoder:
    @classmethod
    def set_value_by_dictitem(cls, instanceOrAttribute, key, value, waarde_shortcut=False):
        attribute_to_set = getattr(instanceOrAttribute, '_' + key)
        if attribute_to_set.field.waardeObject is not None:  # complex / union / KwantWrd / dte

            if isinstance(value, list):
                for index, listitem in enumerate(value):
                    if attribute_to_set.waarde is None or len(attribute_to_set.waarde) <= index:
                        attribute_to_set.add_empty_value()

                    if attribute_to_set.field.waarde_shortcut_applicable and waarde_shortcut:  # dte / kwantWrd
                        attribute_to_set.waarde[index]._waarde.set_waarde(listitem)
                    else:  # complex / union
                        for k, v in listitem.items():
                            cls.set_value_by_dictitem(attribute_to_set.waarde[index], k, v, waarde_shortcut)

            elif isinstance(value, dict):  # only complex / union possible
                if attribute_to_set.waarde is None:
                    attribute_to_set.add_empty_value()

                for k, v in value.items():
                    cls.set_value_by_dictitem(attribute_to_set.waarde, k, v, waarde_shortcut)
            else:  # must be a dte / kwantWrd
                if attribute_to_set.waarde is None:
                    attribute_to_set.add_empty_value()

                attribute_to_set.waarde._waarde.set_waarde(value)
        else:
            attribute_to_set.set_waarde(value)