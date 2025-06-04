from django.urls import path
from . import views

app_name = "telekoko"            
urlpatterns = [
    path("", views.index, name='index'),
]