# # from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer,PersonalInfoSerializer, EducationalInfoSerializer, ExperienceInfoSerializer, SkillsInfoSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PersonalInfo,EducationalInfo,ExperienceInfo,skillsInfo
from rest_framework.permissions import IsAuthenticated



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
    def get(self, request, format=None):
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
        serializer=PersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
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
            return Response({'msg':'Experience Information Update Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
    def delete(self,request,id,format=None):
        user= skillsInfo.objects.filter(user=id)
        user.delete()
        return Response({'msg':'Data Deleted Successfully'})

    






