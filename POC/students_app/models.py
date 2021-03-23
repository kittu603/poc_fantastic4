from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Student(models.Model):
    student_id = models.OneToOneField(User)
    student_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.student_name}"


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    attendance = models.IntegerField()

    def __str__(self):
        return f"{self.attendance} for {self.student.name}"


class StudentCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    student = models.ManyToManyField(Student)
    course_name = models.CharField(max_length=30)
    is_course_available = models.BooleanField()

    def __str__(self):
        return f"{self.course_name}"


class StudentClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(StudentCourse, on_delete=models.PROTECT)
    class_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('class_id', 'course')


class StudentOnlineTest(models.Model):
    test_id = models.IntegerField(primary_key=True)
    test_name = models.CharField(max_length=20)
    course = models.ForeignKey(StudentCourse, on_delete=models.PROTECT)
    student = models.ManyToManyField(Student)
    is_eligible = models.BooleanField()

    def __str__(self):
        return f"{self.test_name}"
