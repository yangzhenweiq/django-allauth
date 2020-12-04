from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import CodelabProvider


urlpatterns = default_urlpatterns(CodelabProvider)
