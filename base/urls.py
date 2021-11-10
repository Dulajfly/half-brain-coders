from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'exitpoint', ExitPointViewSet)

urlpatterns = [
    path('', index, name='base'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_account, name='activate_account'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate_account'),

    path('exitpoint/', ExitPointView.as_view(), name='exitpoint'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/reset_password.html'), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_done.html'), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/reset_password_complete.html'), name='password_reset_complete'),

    url('api/', include(router.urls))

]
