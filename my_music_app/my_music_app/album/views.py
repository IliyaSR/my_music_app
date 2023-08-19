from django.shortcuts import render, redirect
from my_music_app.album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.album.models import Album


def add_alum_page(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('with_profile')

    context = {
        'form': form
    }

    return render(request, template_name='album/add-album.html', context=context)


def album_details_page(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, template_name='album/album-details.html', context=context)


def album_edit_page(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, template_name='album/edit-album.html', context=context)


def album_delete_page(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, template_name='album/delete-album.html', context=context)
