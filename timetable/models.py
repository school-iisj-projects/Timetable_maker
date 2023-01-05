from django.db import models
import uuid


# Create your models here.
class Teacher(models.Model):
    unique_id = models.UUIDField(unique=True,
                                 default=uuid.uuid4,
                                 editable=False,
                                 primary_key=True)
    name = models.CharField(max_length=256)
    subjects = models.JSONField()
    #working_days = models.JSONField()
    subject_acc_class = models.JSONField()
    grades_taught = models.JSONField()


#class Class(models.Model):
# periods_per_week =  models.JSONField()
#homeroom_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
