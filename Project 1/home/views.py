from django.shortcuts import render
from home import models
from home import forms
from django.db.models import Avg
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def musician_view(request):
    musician_list = models.Musician.objects.order_by('-id')
    return render(request, 'home.html', context={
        'title': 'List of The Artist',
        'musician_view': musician_list
    })


def album_view(request):
    album_list = models.Album.objects.all
    return render(request, 'album_view.html', context={
        'album_view': album_list,
        'title': 'All Album List'
    })


def artist_album_view(request, id):
    artist_detail_list = models.Musician.objects.get(pk=id)
    artist_album_list = models.Album.objects.filter(artist=id).order_by('-id')
    artist_album_average = models.Album.objects.filter(artist=id).aggregate(Avg('rating'))
    return render(request, 'album_list.html', context={
        'artist_detail_view': artist_detail_list,
        'artist_album_view': artist_album_list,
        'artist_rating_view': artist_album_average
    })


def artist_edit_view(request, id):
    artist_detail_view = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=artist_detail_view)

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=artist_detail_view)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return artist_album_view(request, id)

    return render(request, 'artist_edit_view.html', context={
        'artist_edit_form': musician_form,
    })


def album_edit_view(request, album_id):
    album_detail_view = models.Album.objects.get(pk=album_id)
    album_form = forms.AlbumForm(instance=album_detail_view)

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album_detail_view)

        if album_form.is_valid():
            album_form.save(commit=True)

    return render(request, 'album_edit_view.html', context={
        'album_edit_form': album_form
    })


def musician_delete_view(request, id):
    artist_detail = models.Musician.objects.get(pk=id).delete()
    return render(request, 'delete.html', context={
        'message': 'Musician Deleted',
    })


def album_delete_view(response, album_id):
    album_details = models.Album.objects.get(pk=album_id).delete()
    return render(response, 'delete.html',
                  context={'tab': 'Album delete',
                           'message': 'Your action has been completed'})


def musician_form_view(request):
    musician_form = forms.MusicianForm()
# FORM SUBMITTING
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return musician_view(request)

    return render(request, 'musician_form.html', context={
        'musician_form_view': musician_form,
        'title': 'Add Artist Form'
    })


def album_form_view(request):
    album_form = forms.AlbumForm()

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)

        if album_form.is_valid():
            album_form.save(commit=True)
            return album_view(request)

    return render(request, 'album_form.html', context={
        'album_form_view': album_form,
        'title': 'Add Album Form',
    })


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_picture' in request.FILES:
                user_info.profile_pic = request.FILES['profile_picture']

            user_info.save()
            registered = True
    else:
        user_form = forms.UserForm()
        user_info_form = forms.UserInfoForm()

    dict = {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered}
    return render(request, 'register.html', context=dict)


def login_page(request):
    return render(request, 'login.html', context={})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active!!")
        else:
            return HttpResponse("Login Details are Wrong!")
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('musician_view'))


def index(request):
    # Fatching Authentic User
    if request.user.is_authenticated:
        current_user = request.user
        id = current_user.id
        user_basic_info = User.objects.get(pk=id)
        user_more_info = models.UserInfo.objects.get(user__pk=id)
        dict = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}

    return render(request, 'index.html', context=dict)
