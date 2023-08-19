from django.shortcuts import render, redirect
from my_music_app.account.models import Profile
from my_music_app.album.models import Album
from my_music_app.home.forms import ProfileCreateForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    if get_profile() is not None:
        return redirect('with_profile')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('with_profile')

    context = {
        'form': form,
        'nav_link': True,

    }
    return render(request, template_name='home/home-no-profile.html', context=context)


def with_profile(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }

    return render(request, template_name='home/home-with-profile.html', context=context)
