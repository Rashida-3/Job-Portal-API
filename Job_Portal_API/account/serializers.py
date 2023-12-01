# from django.shortcuts import render
from rest_framework import serializers
from account.models import User
from .models import PersonalInfo, EducationalInfo,ExperienceInfo,skillsInfo,ProfileInfo
from django.db import models


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this bcoz we need confirm password field in our registration request
    password2= serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs={
            'password':{'write_only':True}
        }

# validating password and confirm password while Registration
    def validate(self, attrs):
        password= attrs.get('password')
        password2= attrs.get('password2')
        if password!= password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=255)
    class Meta:
        model= User
        fields= ['email','password'] 


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        # model=PersonalInfo
        fields=['user','first_name','last_name','gender','date_of_birth','location','phone_no']

# Educational Information

class EducationalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # model=EducationalInfo  
        fields=['user','Institution','degree','field_of_study','start_year','end_year','grade']

        
# Experience Information

class ExperienceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # model=ExperienceInfo
        fields=['user','company','role','year_of_experience','current_ctc']

# Skills Information

class SkillsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # model=skillsInfo
        fields=['user','name','description']        

# Profile informaion

class profileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # model=ProfileInfo
        fields='__all__'


    