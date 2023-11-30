
from django.urls import path, include
from account.views import UserRegistrationView,UserLoginView ,PersonalInfoView,EducationalInfoView,ExperienceInfoView, SkillsInfoView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('personal_info/', PersonalInfoView.as_view(), name='personal_info'),
    path('personal_info/<int:id>', PersonalInfoView.as_view(), name='personal_info'),
    path('educational_info/', EducationalInfoView.as_view(), name='educational_info'),
    path('Educational_Info/<int:id>', EducationalInfoView.as_view(), name='Educational_Info'),
    path('Experience_Info/', ExperienceInfoView.as_view(), name='Experience_Info'),
    path('Experience_Info/<int:id>', ExperienceInfoView.as_view(), name='Experience_Info'),
    path('Skills_Info/', SkillsInfoView.as_view(), name='Skills_Info'),
    path('Skills_Info/<int:id>', SkillsInfoView.as_view(), name='Skills_Info'),







]
