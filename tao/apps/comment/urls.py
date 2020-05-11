from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('<int:users_id>/profile',views.profile,name='profile'),
    path('<int:users_id>/change',views.change,name='change'),
    path('search',views.search,name='search'),
    path('<int:users_id>/profile/edit',views.edit,name='edit'),
    path('<int:users_id>/delete',views.delete,name='delete'),
    path('<int:users_id>/<int:comment_id>/deletecom', views.deletecom, name='deletecom'),
    path('<int:users_id>/adminka',views.adminka,name='adminka'),
    path('about',views.about,name='about'),
    path('<int:users_id>/profile/doedit',views.doedit,name='doedit'),
    path('', views.register, name='register'),
    path('main',views.main,name="main"),
    path('<int:users_id>/', views.prof ,name='prof'),
    path('<int:users_id>/leave_opinion', views.leave_opinion ,name='leave_opinion'),
    path('<int:users_id>/<int:comment_id>/like_change', views.like_change ,name='like_change'),
    path('<int:users_id>/<int:comment_id>/dislike_change', views.dislike_change, name='dislike_change'),
]
