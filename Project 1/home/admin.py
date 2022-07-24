from django.contrib import admin
from home import models

# Register your models here.


class MusicianAdmin(admin.ModelAdmin):
    list_display = ('artistName', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'albumName', 'releaseDate', 'rating')


class UserAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(models.Musician, MusicianAdmin)
admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.UserInfo, UserAdmin)
