from django.urls import path, include
from my_music_app.home.views import home_page, with_profile

urlpatterns = [
    path('', home_page, name='home'),
    path('with_profile/', with_profile, name='with_profile')
]
