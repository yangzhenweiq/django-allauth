from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import AimofaProvider


urlpatterns = default_urlpatterns(AimofaProvider)
