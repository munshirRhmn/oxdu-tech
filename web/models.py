# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models    
from django.utils.text import slugify

class CustomUser(AbstractUser):
    STAFF='1'
    STUDENT='2'
    email = models.EmailField(max_length=100)
    USER_CHOICES = (
        (STAFF, 'staff'),
        (STUDENT, 'student'),
    )
    user_role = models.CharField(choices=USER_CHOICES,max_length=100)
 
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields specific to students

class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields specific to admins

class Course(models.Model):
    course_name=models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.course_name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)

    
class Session(models.Model):
    session_name=models.TextField(null=True)
    session_start=models.IntegerField(null=True)
    session_end=models.IntegerField(null=True)
    
    def __str__(self):
      return self.session_name  

class Student(models.Model):
    gender_choices=(
        ('male','male'),
        ('female','female')
    )

    student_id =models.CharField(max_length=50 ,unique=True)
    slug = models.SlugField(unique=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    student_user=models.CharField(max_length=50)
    student_mail=models.EmailField(max_length=80)
    student_address=models.TextField(max_length=200)
    student_gender=models.CharField(choices=gender_choices,max_length=50)
    student_profilepic=models.ImageField(upload_to="student-images")
    student_year=models.ForeignKey(Session,on_delete=models.CASCADE)
    student_course= models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student_action=models.TextField()

    def __str__(self):
      return self(f"{first_name}+ {last_name}")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self(f"{first_name}+{student_id}"))
        super().save(*args, **kwargs)
    






