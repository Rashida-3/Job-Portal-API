
from django.urls import path, include
from account.views import UserRegistrationView,UserLoginView ,PersonalInfoView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('personal_info/', PersonalInfoView.as_view(), name='personal_info'),


]
