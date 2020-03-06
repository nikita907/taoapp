from django.urls import path
from . import views

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('<int:users_id>/', views.prof ,name='prof'),
    path('<int:users_id>/leave_opinion', views.leave_opinion ,name='leave_opinion')
]