from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('new_diary/', views.new_diary, name='new_diary'),
    path('create_diary/', views.create_diary, name='create_diary'),
    path("<int:diary_id>/delete/", views.delete, name="delete"),
]