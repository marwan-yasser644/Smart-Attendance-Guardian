from django.db import models

class Student(models.Model):  # تأكد إن S حرف كبير
    name = models.CharField(max_length=200)
    parent_phone = models.CharField(max_length=20)
    preferred_language = models.CharField(max_length=2, default='ar')

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date')