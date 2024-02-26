from .views import RegisterationView, UsernameValidateView, LogoutView, EmailValidateView, VerificationView, LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

	path('register', RegisterationView.as_view(), name='register'),
	path('login', LoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('validate-username', csrf_exempt(UsernameValidateView.as_view()), name='validate-username'),
	path('validate-email', csrf_exempt(EmailValidateView.as_view()), name='validate-email'),
	path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
]