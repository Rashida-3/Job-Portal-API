# # from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer,PersonalInfoSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PersonalInfo





# # generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# # Create your views here.

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
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg': 'Personal Information added Successfully'},
            status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PersonalInfoUpdated(APIView):
    renderer_classes=[UserRenderer]  
    # personalInfo_updated=[Isauthenticated]  
    def put(self,request,pk,format=None):
        renderer_classes=[UserRenderer]

        id=pk
        stu= PersonalInfo.objects.get(pk=id)
        serializer= PersonalInfoSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Personal Information Complete Data Updated Successfully'})
        return Response(serializer.errors, status=status.
        HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        renderer_classes=[UserRenderer]

        id=pk
        stu= PersonalInfo.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})




