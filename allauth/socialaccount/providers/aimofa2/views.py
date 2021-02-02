import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import Aimofa2Provider


class Aimofa2OAuth2Adapter(OAuth2Adapter):
    provider_id = Aimofa2Provider.id
    settings = app_settings.PROVIDERS.get(provider_id, {})
    server = settings.get('SERVER_URL', 'http://auth.localhost')
    access_token_url = '{0}{1}'.format(server, settings.get('ACCESS_TOKEN_URL', '/o/token/'))
    authorize_url = '{0}{1}'.format(server, settings.get('AUTHORIZE_URL', '/o/authorize/'))
    profile_url = '{0}{1}'.format(server, settings.get('PROFILE_URL', '/o/user_info/'))

    def complete_login(self, request, app, token, **kwargs):
        headers = {'authorization': 'Bearer {0}'.format(token)}
        try_times = 3  # 重试的次数
        for i in range(try_times):
            try:
                resp = requests.get(self.profile_url, headers=headers, timeout=(3.05, 7))
                # 注意此处也可能是302等状态码
                if resp.status_code == 200:
                    break
            except Exception as ex:
                print('requests failed {i} time')
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login

oauth2_login = OAuth2LoginView.adapter_view(Aimofa2OAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(Aimofa2OAuth2Adapter)
