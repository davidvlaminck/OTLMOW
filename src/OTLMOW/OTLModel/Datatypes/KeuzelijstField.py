import logging
import warnings

from OTLMOW.Facility.Exceptions.RemovedOptionError import RemovedOptionError
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class KeuzelijstField(OTLField):
    options: dict[str, KeuzelijstWaarde] = {}
    codelist = ''

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'{value} is not the correct type. Expecting a string')
            if not value in attribuut.field.options.keys():
                raise ValueError(
                    f'{value} is not a valid option for {attribuut.naam}, find the valid options using .attr_type_info("{attribuut.naam}")')

            option_value = attribuut.field.options[value]
            if option_value.status == 'uitgebruik':
                warnings.warn(message=f'{value} is a deprecated value for {attribuut.naam}, please refrain from using this value.',
                              category=DeprecationWarning)
                logging.warning(f'{value} is a deprecated value for {attribuut.naam}, please refrain from using this value.')
            elif option_value.status == 'verwijderd':
                logging.error(f'{value} is no longer a valid value for {attribuut.naam}.')
                raise RemovedOptionError(f'{value} is no longer a valid value for {attribuut.naam}.')
        return True

    def __str__(self):
        s = f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""
        s += '\npossible values:\n'
        s += '\n'.join(list(map(lambda x: '    ' + x.print(), self.options.values())))
        return s
