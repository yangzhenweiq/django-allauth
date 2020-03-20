from allauth.account.models import EmailAddress
from allauth.socialaccount.app_settings import QUERY_EMAIL
from allauth.socialaccount.providers.base import AuthAction, ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class Scope(object):
    EMAIL = 'email'
    PROFILE = 'profile'


class LonganAccount(ProviderAccount):
    pass
    # def get_profile_url(self):
    #     return self.account.extra_data.get('link')

    # def get_avatar_url(self):
    #     return self.account.extra_data.get('picture')

    # def to_str(self):
    #     dflt = super(LonganAccount, self).to_str()
    #     return self.account.extra_data.get('name', dflt)


class LonganProvider(OAuth2Provider):
    id = 'longan'
    name = 'Longan'
    account_class = LonganAccount

    def get_default_scope(self):
        scope = [Scope.PROFILE]
        if QUERY_EMAIL:
            scope.append(Scope.EMAIL)
        return ['read']

    # def get_auth_params(self, request, action):
    #     ret = super(LonganProvider, self).get_auth_params(request,
    #                                                       action)
    #     if action == AuthAction.REAUTHENTICATE:
    #         ret['prompt'] = 'select_account consent'
    #     return ret

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    username=data.get('username'))

    # def extract_email_addresses(self, data):
    #     ret = []
    #     email = data.get('email')
    #     if email and data.get('verified_email'):
    #         ret.append(EmailAddress(email=email,
    #                    verified=True,
    #                    primary=True))
    #     return ret


provider_classes = [LonganProvider]
