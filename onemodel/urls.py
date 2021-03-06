from django.contrib import admin
from django.urls import path
from . import views

app_name = 'onemodel'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:post_id>/post_detail', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
]