from .views import home, sign_up, logout_user, audits
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('audits/', audits, name='audits'),
    path('accounts/sign_up/',sign_up,name="sign-up"),
    path('accounts/logout/', logout_user, name="logout")
]
