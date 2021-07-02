from django.contrib import admin
from .models import Education, Experience, Publication, Course, Curr_student, Passed_student, Project


# Register your models here.
class EducationsAdmin(admin.ModelAdmin):
    list_display = ('year', 'position', 'institute', 'image_tag', 'add_date')
    search_fields = ('institute', 'position')
    list_per_page = 50


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('duration', 'position', 'company', 'image_tag', 'exp_info', 'add_date')
    search_fields = ('company', 'position')
    list_per_page = 50


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'info', 'type', 'add_date')
    search_fields = ('title', 'author')
    list_per_page = 50


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'times_conducted', 'image_tag', 'about', 'special_position', 'add_date')
    search_fields = ('course_id', 'course_name')
    list_per_page = 50


class Curr_studentAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'year_joining', 'about', 'ed_level', 'image_tag', 'add_date')
    search_fields = ('name', 'ed_level')
    list_per_page = 50


class Passed_studentAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'tenure', 'about', 'ed_level', 'add_date')
    search_fields = ('name', 'ed_level')
    list_per_page = 50


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'tenure', 'project_value', 'pi', 'copi', 'about', 'type', 'add_date')
    search_fields = ('name', 'company')
    list_per_page = 50


admin.site.register(Education, EducationsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Curr_student, Curr_studentAdmin)
admin.site.register(Passed_student, Passed_studentAdmin)
admin.site.register(Project, ProjectAdmin)
