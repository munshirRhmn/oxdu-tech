from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path("",views.home_content,name='home_content'),
    path("add_staff_template",views.add_staff_template,name='add_staff_template'),
    path("manage_student_template",views.manage_student_template,name='manage_student_template'),
    path("add_student_template",views.add_student_template,name='add_student_template'),
    path("manage_course_template",views.manage_course_template,name='manage_course_template'),
    path("add_course_template",views.add_course_template,name='add_course_template'),
    path("manage_session_template",views.manage_session_template,name='manage_session_template'),
    path("add_session_template",views.add_session_template,name='add_session_template'),
    path("admin_view_attendance",views.admin_view_attendance,name='admin_view_attendance'),
    path("student_feedback_template",views.student_feedback_template,name='student_feedback_template'),
    path("student_leave_view",views.student_leave_view,name='student_leave_view'),

    path('edit_course/<slug:slug>',views.edit_course,name='edit_course')
    
]  