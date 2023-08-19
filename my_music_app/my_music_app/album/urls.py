from django.urls import path, include
from my_music_app.album.views import add_alum_page, album_details_page, album_delete_page, album_edit_page

urlpatterns = (
    path('add/', add_alum_page, name='add_album'),
    path('details/<int:pk>/', album_details_page, name='details_album'),
    path('edit/<int:pk>/', album_edit_page, name='edit_album'),
    path('delete/<int:pk>/', album_delete_page, name='delete_album')
)
