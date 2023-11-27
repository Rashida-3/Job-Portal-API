
from django.urls import path
# from account.views import UserRegistrationView,UserLoginView

urlpatterns = [
    path('register/', admin.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    ]
