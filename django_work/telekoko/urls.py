from django.urls import path
from . import views

app_name = "telekoko"            
urlpatterns = [
    path("", views.index, name='index'),
    path("telekoko/create/",views.feeling_create, name = "feeling_create")
]