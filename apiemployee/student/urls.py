from django.urls import path
from . import views


urlpatterns = [
       path('api/',views.StudentApi.as_view()),
       path('api/<int:pk>',views.StudentApiOne.as_view()),
       path('create/',views.StudentCreateApi.as_view()),
       path('update/<int:pk>',views.StudentUpdateApi.as_view()),
       path('delete/<int:pk>',views.StudentDeleteApi.as_view()),
]
