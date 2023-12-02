
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from account.views import UserRegistrationView,UserLoginView ,PersonalInfoView,EducationalInfoView,ExperienceInfoView, SkillsInfoView,UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('personal_info/', PersonalInfoView.as_view(), name='personal_info'),
    path('personal_info/<int:id>', PersonalInfoView.as_view(), name='personal_info'),
    path('educational_info/', EducationalInfoView.as_view(), name='educational_info'),
    path('educational_info/<int:id>', EducationalInfoView.as_view(), name='Educational_Info'),
    path('experience_info/', ExperienceInfoView.as_view(), name='Experience_Info'),
    path('experience_info/<int:id>', ExperienceInfoView.as_view(), name='Experience_Info'),
    path('skills_info/', SkillsInfoView.as_view(), name='Skills_Info'),
    path('skills_info/<int:id>', SkillsInfoView.as_view(), name='Skills_Info'),
    path('user_profile/', UserProfileView.as_view(), name='User_Profile'),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)[0]

]
