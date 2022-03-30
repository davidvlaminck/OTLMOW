from OTLMOW.Facility.CertRequester import CertRequester
from OTLMOW.Facility.JWTRequester import JWTRequester


class RequesterFactory:
    @classmethod
    def create_requester(cls, settings=None, auth_type='', env=''):
        try:
            auth_info = next(a for a in settings['auth_options'] if a['type'] == auth_type and a['environment'] == env)
        except StopIteration:
            raise ValueError(f"Could not load the settings for {auth_type} {env}")

        first_part_url = ''
        if auth_info['environment'] == 'prd':
            first_part_url = 'https://services.apps.mow.vlaanderen.be/'
        elif auth_info['environment'] == 'tei':
            first_part_url = 'https://services.apps-tei.mow.vlaanderen.be/'
        elif auth_info['environment'] == 'dev':
            first_part_url = 'https://services.apps-dev.mow.vlaanderen.be/'

        if auth_info['type'] == 'JWT':
            return JWTRequester(private_key_path=auth_info['key_path'],
                                client_id=auth_info['client_id'],
                                first_part_url=first_part_url)
        if auth_info['type'] == 'cert':
            return CertRequester(cert_path=auth_info['cert_path'],
                                 key_path=auth_info['key_path'],
                                 first_part_url=first_part_url)
