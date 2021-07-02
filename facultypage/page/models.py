from django.db import models
from django.utils.html import format_html


# Create your models here.

# for education
class Education(models.Model):
    ed_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    image = models.ImageField(upload_to='education/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for experience
class Experience(models.Model):
    ex_id = models.AutoField(primary_key=True)
    duration = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='experience/')
    exp_info = models.TextField(max_length=5000)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for publication
class Publication(models.Model):
    pub_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    info = models.TextField(max_length=5000)
    publication_choices = [
        ('Patents', 'Patents'), ('Conferences', 'Conferences'), ('Journals', 'Journals'),
        ('Book_Chapters', 'Book_Chapters')
    ]
    type = models.CharField(
        choices=publication_choices,
        default='Patents',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for courses
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    times_conducted = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course/')
    about = models.TextField(max_length=5000)
    special_position = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for current students
class Curr_student(models.Model):
    cstu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    year_joining = models.CharField(max_length=20)
    about = models.TextField(max_length=5000)
    edlevel_choices = [
        ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Research Scholar', 'Research Scholar')
    ]
    ed_level = models.CharField(
        choices=edlevel_choices,
        default='Research Scholar',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='student/')

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for current students
class Passed_student(models.Model):
    pstu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    tenure = models.CharField(max_length=50)
    about = models.TextField(max_length=5000)
    edlevel_choices = [
        ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Research Scholar', 'Research Scholar')
    ]
    ed_level = models.CharField(
        choices=edlevel_choices,
        default='Research Scholar',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for projects
class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    tenure = models.CharField(max_length=50)
    project_value = models.CharField(max_length=50)
    pi = models.CharField(max_length=100)
    copi = models.CharField(max_length=100)
    about = models.TextField(max_length=5000)
    pr_choices = [
        ('Consultancy', 'Consultancy'), ('Sponsored', 'Sponsored')
    ]
    type = models.CharField(
        choices=pr_choices,
        default='Consultancy',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)
