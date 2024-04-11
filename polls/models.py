from django.db import models

# Create your models here.
#class Course(models.Model):
#    title = models.CharField(max_length=200)
#    description = models.CharField(max_length=200)
#    full_text = models.TextField()
#    image = models.FileField(upload_to="uploads", null=True)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag_id = models.IntegerField()
    theme_id = models.IntegerField()
    theacher_id = models.IntegerField()

class user_course(models.Model):
    studemt_id = models.IntegerField()
    course_id = models.IntegerField()

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    parentname = models.CharField(max_length=30)
    is_teacher = models.BooleanField()
    group = models.CharField(max_length=9)
    photo = models.FileField(upload_to="uploads", null=True)
    discription = models.TextField()
    phone = models.IntegerField()

class course_theme(models.Model):
    course_id = models.PositiveIntegerField()
    theme_id = models.PositiveIntegerField()

class Theme(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=150)
    tag_id = models.PositiveIntegerField()
    tasks_id = models.PositiveIntegerField()

class theme_task(models.Model):
    title = models.IntegerField()
    discription = models.CharField(max_length=50)
    tag_id = models.PositiveIntegerField()
    theme_id = models.PositiveIntegerField()
    teacher_id = models.PositiveIntegerField()

class Task(models.Model):
    title = models.CharField(max_length=50)
    condition = models.CharField(max_length=1500)
    input_format = models.CharField(max_length=120)
    output_format = models.CharField(max_length=120)
    note = models.CharField(max_length=200)
    deadline = models.DateField()
    max_score = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    memoty_linit = models.PositiveIntegerField()

class Test(models.Model):
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    task_id = models.PositiveIntegerField()

class submission_test(models.Model):
    submission_id = models.PositiveIntegerField()
    score = models.PositiveIntegerField()

class Submission(models.Model):
    user_id = models.PositiveIntegerField()
    task_id = models.PositiveIntegerField()
    date = models.DateField()
    status = models.BooleanField()
    progamming_language_id = models.PositiveIntegerField()
    time_of_work = models.TimeField()
    user_code = models.CharField(max_length=1000)
    memory_in_work = models.PositiveIntegerField()
    user_output = models.CharField(max_length=1000)

class Programming_language(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)

