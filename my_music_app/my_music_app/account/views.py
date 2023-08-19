from django.shortcuts import render, redirect
from my_music_app.account.models import Profile
from my_music_app.album.models import Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def profile_details_page(request):
    profile = get_profile()
    album_count = Album.objects.count()

    context = {
        'profile': profile,
        'album_count' : album_count
    }
    return render(request, template_name='accounts/profile-details.html', context=context)


def profile_delete_page(request):
    if request.method == 'POST':
        profile = get_profile()
        albums = Album.objects.all()
        profile.delete()
        albums.delete()
        return redirect('home')

    return render(request, template_name='accounts/profile-delete.html')
