from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('competition/',views.competition,name='competition'),
    path('competition/form/',views.Forms,name="register_form"),
    path('Donate/',views.Donate,name='Donate'),
    path('verified/',views.verify,name="verify")
]