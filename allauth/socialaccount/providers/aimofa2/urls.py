from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import Aimofa2Provider


urlpatterns = default_urlpatterns(Aimofa2Provider)
