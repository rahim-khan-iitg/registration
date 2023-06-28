from django.urls import path
from . import views
urlpatterns=[
    path('signup/',views.register,name='register'),
    path('login/',views.Login, name='login'),
    path('send_otp/',views.send_otp,name="send_otp"),
    path('logout/',views.Logout,name='logout')
]