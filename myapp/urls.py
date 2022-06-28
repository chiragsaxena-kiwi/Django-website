from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views





urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('contact/', views.contact, name="n4"),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout'),
    path('faq',views.faq,name='faq'),
    path('services/',views.services,name='services'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
