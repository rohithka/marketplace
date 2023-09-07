from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import Loginform

app_name = 'core'

urlpatterns = [
    path("",views.index,name="index"),
    path('contacts/',views.contacts,name="contacts"),
    path("sighnup",views.sighnup,name="sighnup"),
    path('login',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=Loginform),name="login"),


]