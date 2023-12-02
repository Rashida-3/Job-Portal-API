from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# custome user manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,verbose_name='Email',unique=True)
    name = models.CharField(max_length=255)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # simplest possible answer: Yes always
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'? "
        #simplest possible answer:Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a number of staff?"
        # simplest possible answer: All admins are staff
        return self.is_admin

# Personal Information model
class PersonalInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=255)
    category=(
        ('Male','male'),
        ('Female','female'),
        ('other','other'),
    )
    gender=models.CharField(max_length=200,choices=category)
    date_of_birth=models.DateField()
    location=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
    
# Educational Information model
class EducationalInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Institution=models.CharField(max_length=250)
    degree=models.CharField(max_length=255)
    field_of_study=models.CharField(max_length=50)
    start_year=models.IntegerField()
    end_year=models.IntegerField()
    grade=models.IntegerField()


    def __str__(self):
        return self.grade
    

    # User Experience model

class ExperienceInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.CharField(max_length=255)
    role=models.CharField(max_length=100)
    # location=models.CharField(max_length=100)
    year_of_experience=models.FloatField()
    current_ctc=models.FloatField()

    def __str__(self):
        return self.role

# Skills Model

class skillsInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

# Profile information

class ProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='media/image/avtar1.png', upload_to='media/image')

    def __str__(self):
        return str(self.user)

def created_profile(sender, instance, created, **kwargs):
    if created:
        ProfileInfo.objects.create(user=instance)
        print('Profile Created')   
post_save.connect(created_profile, sender=User)        


















