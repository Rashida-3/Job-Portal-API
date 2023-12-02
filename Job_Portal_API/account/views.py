# # from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer,PersonalInfoSerializer, EducationalInfoSerializer, ExperienceInfoSerializer, SkillsInfoSerializer,profileInfoSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PersonalInfo,EducationalInfo,ExperienceInfo,skillsInfo,ProfileInfo
from rest_framework.permissions import IsAuthenticated
from django.core.signals import request_finished
from django.shortcuts import get_object_or_404


# # generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# # Create your views here.
# Registration and Login 

class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            token=get_tokens_for_user(user)

            return Response({'token':token,'msg': 'Registration Successful'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer= UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email= serializer.data.get('email')
            password= serializer.data.get('password')
            user= authenticate(email=email, password=password)
            if user is not None:
                token=get_tokens_for_user(user)

                return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.
        HTTP_400_BAD_REQUEST)
    
class PersonalInfoView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        user = request.user
        serializer=PersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save(user=user)
            return Response({'msg': 'Personal Information added Successfully'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id, format=None):
        user=PersonalInfo.objects.get(user=id)
        serializer= PersonalInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Update Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
    def delete(self,request,id,format=None):
        user= PersonalInfo.objects.filter(user=id)
        user.delete()
        return Response({'msg':'Data Deleted'})
    

  # Educational Information

class EducationalInfoView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,formate=None):
        user = request.user
        if EducationalInfo.objects.filter(user=user).exists():
            return Response({'error': 'Eduction already exists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=EducationalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({'msg': 'Educational Information added Successfully'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,id,formate=None):
        user=EducationalInfo.objects.get(user=id)
        serializer= EducationalInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Educational Information Update Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
    def delete(self,request,id,format=None):
        user= EducationalInfo.objects.filter(user=id)
        user.delete()
        return Response({'msg':'Data Deleted Successfully'})
    

      # Experience Information

class ExperienceInfoView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,formate=None):
        user = request.user
        if ExperienceInfo.objects.filter(user=user).exists():
            return Response({'error': 'Experience already exists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=ExperienceInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({'msg': 'Experience Information added Successfully'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,id,formate=None):
        user=ExperienceInfo.objects.get(user=id)
        serializer= ExperienceInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Experience Information Update Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
    def delete(self,request,id,format=None):
        user= ExperienceInfo.objects.filter(user=id)
        user.delete()
        return Response({'msg':'Data Deleted Successfully'})
    
    # Skills information

class SkillsInfoView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,formate=None):
        serializer=SkillsInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({'msg': 'Skills Information added Successfully'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request,id,formate=None):
        user=skillsInfo.objects.get(user=id)
        serializer= SkillsInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Skills Information Update Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
    def delete(self,request,id,format=None):
        user= skillsInfo.objects.filter(user=id)
        user.delete()
        return Response({'msg':'Data Deleted Successfully'})
    

class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        user=request.user
        
        try: 
            profile=ProfileInfo.objects.get(user=user)
            print('DEBUG......',profile,user.id)
            print('DEBUG......',PersonalInfo.objects.get(user=user))
            personal_info=PersonalInfo.objects.get(user=user)

            education_info=EducationalInfo.objects.get(user=user.id)
            experience=ExperienceInfo.objects.get(user=user.id)
            skills=skillsInfo.objects.get(user=user)
            print('DEBUG ----------- .',skills)


            profile_serializer=profileInfoSerializer(profile)
            personal_serializer=PersonalInfoSerializer(personal_info)
            education_serialize=EducationalInfoSerializer(education_info)
            experience_serializer=ExperienceInfoSerializer(experience)
            skills_serializer=SkillsInfoSerializer(skills)

            response_data={
                'profile':profile_serializer.data,
                'personal_info':personal_serializer.data,
                'education_info':education_serialize.data,
                'experience':experience_serializer.data,
                'skills':skills_serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        except (ProfileInfo.DoesNotExist, PersonalInfo.DoesNotExist, EducationalInfo.DoesNotExist,ExperienceInfo.DoesNotExist,skillsInfo.DoesNotExist):
            return Response({'massage': 'User Profile Does not Exit'}, status=status.HTTP_404_NOT_FOUND)

        
















    






