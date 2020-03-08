from django.urls import path
from . import views

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('<int:users_id>/', views.prof ,name='prof'),
    path('<int:users_id>/leave_opinion', views.leave_opinion ,name='leave_opinion'),
    path('<int:users_id>/<int:comment_id>/like_change', views.like_change ,name='like_change'),
    path('<int:users_id>/<int:comment_id>/dislike_change', views.dislike_change, name='dislike_change')
]