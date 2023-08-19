from django.contrib import admin
from my_music_app.album.models import Album


class AlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)
