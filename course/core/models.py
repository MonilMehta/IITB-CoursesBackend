from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)  # Title of the course
    course_code = models.CharField(max_length=20, unique=True)  # Unique course code
    description = models.TextField()  # Description of the course

    def __str__(self):
        return f"{self.course_code} - {self.title}"

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances') 
    year = models.IntegerField() 
    semester = models.IntegerField() 

    def __str__(self):
        return f"{self.course.course_code} - {self.year} Semester {self.semester}"
    
    class Meta:
        unique_together = ('course', 'year', 'semester') 