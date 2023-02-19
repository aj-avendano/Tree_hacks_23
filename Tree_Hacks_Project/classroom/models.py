from django.db import models

# Create your models here.
#Teacher
####names
####subject
####assignments[many to one]
##class Teacher(models.Models):
##    name=models.CharField(max_length=30)
##    subject=models.CharField(max_length=30)
##    assignments=models.CharField(max_length=30)#foreign key
#Student
###name
###uncompleted assignments
###completed assignments
##class Student(models.Models):
##    name=models.CharField(max_length=30)
#Asignment
###subject
###teacher
###questions
##class Assignment(models.Models):
##    teacher=models.CharField(max_length=30)#foreign key[many to one]
##    subject=models.CharField(max_length=30)
##    questions=models.CharField(max_length=30)#foreign key[many to one]
#Question
###teacher_instuctions
###assignment
###question_prompt
###student_image_Description
##class Question(models.Models):
##    teacher_instuctions=models.CharField(max_length=30)
##    assignment=models.CharField(max_length=30)#foreign key
##    question_prompt=models.CharField(max_length=30)
##    student_image_description=models.CharField(max_length=30)
##    generated_image_url=models.CharField(max_length=30)
