from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Users, Comment, AdditionalComments
from django.urls import reverse
from django.utils import timezone


def prof(request, users_id):
    try:
        a = Users.objects.get(id=users_id)
    except:
        raise Http404("Такого пользователя нет")

    commen = a.comment_set.all()
    return render(request, 'comment/prof.html', {'User': a, 'commen': commen})


def leave_opinion(request, users_id):
    try:
        a = Users.objects.get(id=users_id)
    except:
        raise Http404("Такого пользователя нет")

    a.comment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'], comment_likes='0',
                         comment_dislikes='0', pub_date=timezone.now())
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
    return render(request, 'comment/start.html', {})
