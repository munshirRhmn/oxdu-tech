from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course,Session,Student
from .models import CustomUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_content(request):      
    return render(request, 'staff-templates/home_content.html')


# def home_content(request):
#     return render(request,'staff-templates/home_content.html')

def add_staff_template(request):
    return render(request,'staff-templates/add_staff_template.html')

def manage_student_template(request):
    students = Student.objects.all()
    context={
        'students':students
    }
    return render(request,'staff-templates/manage_student_template.html',context)

def add_student_template(request):
    return render(request,'staff-templates/add_student_template.html')

def manage_course_template(request):
    course=Course.objects.all()
    context={
        'courses':course
    }
    return render(request,'staff-templates/manage_course_template.html',context)

def add_course_template(request):
    if request.method=="POST":
        course = request.POST.get('course')
       
        course_save = Course(
            course_name=course

        )
        course_save.save() 
    return render(request,'staff-templates/add_course_template.html')

def edit_course(request,slug):
    # course = get_object_or_404(Course,slug)
    course = Course.objects.filter(slug=slug)
    context ={
        'courses':course
    }
    return render(request,'staff-templates/edit_course_template.html',context)
   

def manage_session_template(request):
    return render(request,'staff-templates/manage_session_template.html')

def add_session_template(request):
    # if request.method=="POST":
    #     session_start_year = request.POST.get('session_start_year')
    #     session_end_year = request.POST.get('session_end_year')

    #     session_save = Session(
             
    #     )
    return render(request,'staff-templates/add_session_template.html')

def admin_view_attendance(request):
    return render(request,'staff-templates/admin_view_attendance.html')

def student_feedback_template(request):
    return render(request,'staff-templates/student_feedback_template.html')

def student_leave_view(request):
    return render(request,'staff-templates/student_leave_view.html')