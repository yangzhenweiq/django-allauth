import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import LonganProvider


class LonganOAuth2Adapter(OAuth2Adapter):
    provider_id = LonganProvider.id
    # access_token_url = 'https://accounts.longan.link/o/oauth2/token'
    # authorize_url = 'https://accounts.longan.link/o/oauth2/auth'
    # profile_url = 'https://www.googleapis.com/oauth2/v1/userinfo'

    settings = app_settings.PROVIDERS.get(provider_id, {})
    server = settings.get('SERVER_URL', 'http://auth.localhost')
    access_token_url = '{0}/o/token/'.format(server)
    authorize_url = '{0}/o/authorize/'.format(server)
    profile_url = '{0}/api/users/me/'.format(server)

    def complete_login(self, request, app, token, **kwargs):
        headers = {'authorization': 'Basic {0}'.format(token)}
        resp = requests.get(self.profile_url, headers=headers)
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(LonganOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(LonganOAuth2Adapter)
