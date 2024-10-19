from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'  # Match your MySQL table name
    
    def __str__(self):
        return self.name  # For Student model


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'course'  # Match your MySQL table name

    def __str__(self):
        return self.course_name

class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

    class Meta:
        db_table = 'student_courses'  # Match your MySQL table name
        unique_together = (('student_id', 'course_id'),)  # To match the primary key constraint
