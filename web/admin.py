from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser,Course,Session,Student
class UserRoleAdmin(UserAdmin):
    list_display=('email',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(CustomUser,UserRoleAdmin)

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("course_name",)}
    list_display = ('course_name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Course, CourseAdmin)

admin.site.register(Session)


class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("student_id","first_name")}
    list_display = ('first_name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)