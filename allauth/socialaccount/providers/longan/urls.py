from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import LonganProvider


urlpatterns = default_urlpatterns(LonganProvider)
