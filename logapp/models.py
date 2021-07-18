from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_roll_no = models.CharField(max_length=100)
    s_regd_no = models.CharField(max_length=100)
    s_address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


