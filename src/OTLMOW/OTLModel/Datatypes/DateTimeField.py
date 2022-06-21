import datetime
import logging
from datetime import timedelta
from random import randrange

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class DateTimeField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime."""
    naam = 'DateTime'
    objectUri = 'http://www.w3.org/2001/XMLSchema#dateTime'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime.'
    label = 'Datumtijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#dateTime'

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        return True

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if isinstance(value, bool):
            raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            if log_warnings:
                logging.warning(
                    'Assigned a date to a datetime datatype. Automatically converted to the correct type. Please change the type')
            return datetime.datetime(year=value.year, month=value.month, day=value.day, hour=0, minute=0, second=0)
        if isinstance(value, int):
            if log_warnings:
                logging.warning(
                    'Assigned a int to a datetime datatype. Automatically converted to the correct type. Please change the type')
            timestamp = datetime.datetime.fromtimestamp(value)
            return datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
        if isinstance(value, str):
            try:
                if 'T' in value:
                    dt = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                else:
                    dt = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                if log_warnings:
                    logging.warning(
                        'Assigned a string to a datetime datatype. Automatically converted to the correct type. Please change the type')
                return dt
            except ValueError:
                try:
                    if 'T' in value:
                        dt =  datetime.datetime.strptime(value, "%d/%m/%YT%H:%M:%S")
                    else:
                        dt = datetime.datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
                    if log_warnings:
                        logging.warning(
                            'Assigned a string to a datetime datatype. Automatically converted to the correct type. Please change the type')
                    return dt
                except Exception:
                    raise CouldNotConvertToCorrectTypeError(
                        f'{value} could not be converted to correct type (implied by {cls.__name__})')
        try:
            return datetime.datetime(value)
        except Exception:
            raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def value_default(value):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)

    @staticmethod
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @staticmethod
    def create_dummy_data():
        return DateTimeField.random_date(start=datetime.datetime(2000, 1, 1, 0, 0, 0), end=datetime.datetime(2020, 1, 1, 0, 0, 0))
