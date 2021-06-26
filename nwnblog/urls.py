
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('addpost/',views.add_post, name='addpost'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.user_signin, name='signin'),
    path('signout/',views.user_signout, name='signout'),
]
