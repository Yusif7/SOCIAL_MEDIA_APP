from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usersApp'

urlpatterns = [

    path('', views.home, name='home'),

    # auth
    path('login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # password change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html',
                                                                   success_url='done/'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

    # password_reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', success_url='done/'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm', success_url='complete/'),
         name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # Registration
    path('register/', views.register, name='register'),

    # Profile
    path('edit/', views.edit, name='edit'),
]
