from django.urls import path
from my_music_app.account.views import profile_details_page, profile_delete_page

urlpatterns = [
    path('details/', profile_details_page, name='profile_details'),
    path('delete/', profile_delete_page, name='profile_delete')
]
