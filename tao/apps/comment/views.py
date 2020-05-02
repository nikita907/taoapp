from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms  import  UserRegistrationForm,ImageForm,UserInfoForm

from .models import Users, Comment, AdditionalComments,Image
from django.urls import reverse
from django.utils import timezone
from django.contrib import auth


def prof(request, users_id):
    try:
        a = Users.objects.get(id=users_id)
        try:
            image=a.image_set.get()
        except:
            image=None
    except:
        raise Http404("Такого пользователя нет")

    commen = a.comment_set.all()
    return render(request, 'comment/prof.html', {'im':image,'User': a, 'commen': commen})


def leave_opinion(request, users_id):
    try:
        a = Users.objects.get(id=users_id)
    except:
        raise Http404("Такого пользователя нет")
    temp=len(request.POST['text'])
    try:
        request.POST['name']
        if(temp>=5):
           a.comment_set.create(comment_author='anonim', comment_text=request.POST['text'], comment_likes='0',
                             comment_dislikes='0', pub_date=timezone.now())
        else:
           return HttpResponseRedirect(reverse('prof',args=(a.id,)))
    except:
        if (temp >= 5):
            a.comment_set.create(comment_author=auth.get_user(request).username, comment_text=request.POST['text'], comment_likes='0',
                                 comment_dislikes='0', pub_date=timezone.now())
        else:
            return HttpResponseRedirect(reverse('prof', args=(a.id,)))
    return HttpResponseRedirect(reverse('prof', args=(a.id,)))


def like_change(request,users_id,comment_id):
    a = Users.objects.get(id=users_id)
    b = Comment.objects.get(id=comment_id)
    b.comment_likes = int(b.comment_likes) + 1
    b.save()
    return HttpResponseRedirect(reverse('prof', args=(a.id,)))

def dislike_change(request,users_id,comment_id):
    a = Users.objects.get(id=users_id)
    b = Comment.objects.get(id=comment_id)
    b.comment_dislikes = int(b.comment_dislikes) + 1
    b.save()
    return HttpResponseRedirect(reverse('prof', args=(a.id,)))


def post_list(request):
    return render(request, 'registration/login.html', {})

def register(request):
    a = Users.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            username = user_form.cleaned_data.get('username')
            email=user_form.cleaned_data.get('email')
            a.create(users_nick=username,users_email=email)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
def main(request):
    a = Users.objects.all()
    search_q = request.GET.get('search', '')
    im=Image.objects.all()
    comments=Comment.objects.all()
    try:
        infa=a.userinfo_set.get()
    except:
        infa=None
    if search_q:
        q = Users.objects.filter(users_nick__icontains=search_q)
    else:
        q = None
    usernick=auth.get_user(request).username
    for c in a:
        if c.users_nick == usernick:
            idishnik = c.id
            break
        else:
            idishnik=1
    b = Users.objects.get(id=idishnik)
    a=Users.objects.exclude(id=idishnik)
    return render(request, 'comment/main.html', {'im':im,'Comments':comments,'Users': a,'SearchUser':q,'username': auth.get_user(request).username,'spec':b})
def logout(request):
    return render(request,'registration/logged_out')
def profile(request,users_id):
    a = Users.objects.get(id=users_id)
    try:
        infa=a.userinfo_set.get()
    except:
        infa=None
    if a.userOnRedaction:
        uform = UserInfoForm(request.POST, request.FILES or None)
        a.userOnRedaction=False
        a.save()
    else:
        uform=None
    try:
        Images = a.image_set.get()
        form = ImageForm(request.POST, request.FILES or None)
    except:
        form = ImageForm(request.POST, request.FILES or None)
        if request.method == 'POST' and form.is_valid():
            a.image_set.create(photo=request.FILES['photo'],user_has_photo=True)
            a.save()
            Image = a.image_set.get()
        else:
            Image=None
        Images = Image
    commen = a.comment_set.all()
    return render(request, 'comment/profile.html', {'User': a, 'Commen': commen, 'im': Images,'form': form,'uform':uform,'infa':infa})
def change(request,users_id):
    a = Users.objects.get(id=users_id)
    Images = a.image_set.get()
    Images.delete()
    form = ImageForm(request.POST, request.FILES or None)
    a.image_set.create(photo=request.FILES['photo'], user_has_photo=True)
    a.save()
    return profile(request, users_id)
def search(request):
    search_q = request.GET.get('search','')
    if search_q:
        a = Users.objects.filter(users_nick__icontains=search_q)
    else:
        raise Http404("Такого пользователя нет")
    return render(request, 'comment/main.html', {'Users': a})
def edit(request,users_id):
    a=Users.objects.get(id=users_id)
    try:
        temp=a.userinfo_set.get()
        temp.delete()
        a.save()
    except:
        None
    a.userOnRedaction=True
    a.save()
    return HttpResponseRedirect(reverse('profile',args=(a.id,)))
def doedit(request,users_id):
    a = Users.objects.get(id=users_id)
    form = ImageForm(request.POST, request.FILES or None)
    a.userinfo_set.create(userAge=request.POST['userAge'], userTown=request.POST['userTown'],userSex=request.POST['userSex'], userCountry=request.POST['userCountry'],userAbout=request.POST['userAbout'])
    a.userOnRedaction = False
    a.save()
    return HttpResponseRedirect(reverse('profile', args=(a.id,)))















