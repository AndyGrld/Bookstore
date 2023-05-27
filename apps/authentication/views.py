import os

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile
from book.models import Book

# Create your views here.


def signup(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            content.update({'error': 'Password mismatch'})
            print(content)
            return render(request, 'authentication/signup.html')
        User.objects.create_user(username=username, email=email, password=pass1)
        Profile.objects.create(user=get_object_or_404(User, username=username))
        return redirect('authentication:signin')
    return render(request, 'authentication/signup.html')


def signin(request):
    users = User.objects.all()
    exists = False
    content = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        for user in users:
            if user.username == username:
                exists = True
        if not exists:
            # email does not exist
            content.update({'error': 'Wrong email'})
            print(content)
            return render(request, 'authentication/sign-in.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:profile')
        else:
            # Wrong password
            content.update({'error': 'Wrong password'})
            print(content)
    return render(request, 'authentication/sign-in.html')


@login_required(login_url='authentication:signin')
def signout(request):
    logout(request)
    return redirect('authentication:signin')


@login_required(login_url='authentication:signin')
def profile(request):
    print(request.path)
    current_profile = get_object_or_404(Profile, user=request.user)
    profile_books = Book.objects.filter(author=current_profile)
    content = {'current_profile': current_profile,
               'profile_books': profile_books}
    return render(request, 'authentication/myprofile.html', content)


@login_required(login_url='authentication:signin')
def profileEdit(request):
    current_profile = get_object_or_404(Profile, user=request.user)
    content = {'current_profile': current_profile}
    if request.method == 'POST':
        profile_pic = request.FILES.get('profilePic')
        username = request.POST.get('username')
        genre = request.POST.get('genre')
        bio = request.POST.get('bio')
        if profile_pic:
            if current_profile.profilePic:
                os.remove(os.path.join(settings.MEDIA_ROOT, current_profile.profilePic.name))
            current_profile.profilePic = profile_pic
        current_profile.user.username = username
        current_profile.genre = genre
        current_profile.bio = bio
        current_profile.save()
        return redirect('authentication:profile')
    return render(request, 'authentication/profileEdit.html', content)


@login_required(login_url='authentication:signin')
def publish(request):
    current_profile = get_object_or_404(Profile, pk=request.user.pk)
    if request.method == 'POST':
        # todo: fix file upload
        book = request.FILES.get('book')
        cover = request.FILES.get('cover')
        title = request.POST.get('title')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        Book.objects.create(
            author=current_profile,
            title=title,
            cover=cover,
            book=book,
            description=description,
            genre=genre
        )
        return redirect('authentication:profile')
    return render(request, 'authentication/publish.html')
