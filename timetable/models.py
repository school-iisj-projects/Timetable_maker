"""from django.db import models
from rest_framework import serializers

import uuid


# Create your models here.
class Teacher(models.Model):
    unique_id = models.UUIDField(unique=True,
                                 default=uuid.uuid4,
                                 editable=False,
                                 primary_key=True)
    name = models.CharField(max_length=256)
    subjects = serializers.ListField()
    #working_days = serializers.ListField()
    subject_acc_class = models.JSONField()
    grades_taught = serializers.ListField()


#class Class(models.Model):
# periods_per_week =  serializers.ListField()
#homeroom_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
class Timetable(models.Model):
  for i in range(1, 13):
      globals()[f"class_{i}_timetable"] = models.JSONField(default=None)
  def sort(self, periods, len_per, teachers, lunch_periodtime):
      #Put sorting algorithm here
      s = False

      #After sotring
      s = True
      ""
  '''for i in range(1, 13):
    globals()[f"self.class_{i}_timetable"] = models.JSONField(default=None)
  s = self.objects.create(self.class_1_timetable, self.class_2_timetable, self.class_3_timetable, self.class_4_timetable, self.class_5_timetable, self.class_6_timetable, self.class_7_timetable, self.class_8_timetable, self.class_9_timetable, self.class_10_timetable, self.class_11_timetable, self.class_12_timetable)'''
      #S should be time timeable class which should be returned
      #Otherwise if sorting was not possible, then s should be the error which should be returned and shown by the app
       

  def show_timetable(self, request):
    self.sort()
    self.timetable = {"grade_1":self.class_1_timetable, "grade_2":self.class_2_timetable, "grade 3": self.class_3_timetable, "grade_4":self.class_4_timetable, "grade_5":self.class_5_timetable, "grade_6":self.class_6_timetable,"grade_7":self.class_7_timetable, "grade_8":self.class_8_timetable, "grade_9":self.class_9_timeable, "grade_10":self.class_10_timetable, "grade_11":self.class_11_timetable, "grade_12":self.class_12_timetable }
    return self.timetable
    """

from django.db import models
from rest_framework import serializers
import datetime
import uuid


# Create your models here.
class Teacher(models.Model):
    unique_id = models.UUIDField(unique=True,
                                 default=uuid.uuid4,
                                 editable=False,
                                 primary_key=True)
    name = models.CharField(max_length=256)
    subjects = serializers.ListField()
    # working_days = serializers.ListField()
    subject_acc_class = models.JSONField()
    grades_taught = serializers.ListField()


# class Class(models.Model):
# periods_per_week =  serializers.ListField()
# #homeroom_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
# class Timetable(models.Model):

#     for i in range(1, 13):
#         globals()[f"class_{i}_timetable"] = models.JSONField(default=None)

#     def sort(self, periods, len_per, teachers, lunch_periodtime):
#         # Put sorting algorithm here
#         s = False

#         # After sotring
#         s = True
#         ""
#     '''
#   make something so that the variables r defined when any other function access it
#   for i in range(1, 13):
#     globals()[f"self.class_{i}_timetable"] = models.JSONField(default=None)
#   s = self.objects.create(self.class_1_timetable, self.class_2_timetable, self.class_3_timetable, self.class_4_timetable, self.class_5_timetable, self.class_6_timetable, self.class_7_timetable, self.class_8_timetable, self.class_9_timetable, self.class_10_timetable, self.class_11_timetable, self.class_12_timetable)'''
#     # S should be time timeable class which should be returned
#     # Otherwise if sorting was not possible, then s should be the error which should be returned and shown by the app


#     def show_timetable(self, request):
#         self.sort()
#         self.timetable = {"grade_1": self.class_1_timetable, "grade_2": self.class_2_timetable, "grade 3": self.class_3_timetable, "grade_4": self.class_4_timetable, "grade_5": self.class_5_timetable, "grade_6": self.class_6_timetable,
#                           "grade_7": self.class_7_timetable, "grade_8": self.class_8_timetable, "grade_9": self.class_9_timeable, "grade_10": self.class_10_timetable, "grade_11": self.class_11_timetable, "grade_12": self.class_12_timetable}
#         return self.timetable
class Timetable(models.Model):
    periods = models.IntegerField(default=10)
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True)
    lunch_period = models.IntegerField(default=5)
    len_per_period = models.IntegerField(default=40)
    no_of_teachers = models.IntegerField(default=10)
    start_time = models.TimeField(blank=True,
                                  default=datetime.time(hour=9,
                                                        minute=0,
                                                        second=0))
    end_time = models.TimeField(blank=True,
                                default=datetime.time(hour=15,
                                                      minute=0,
                                                      second=0))

    def __str__(self):
        return (f"Timetable {self.id}")
      
    def make_class_dict(self):
        # Takes the teachers taught and arranges them by grades which they teach
        pass

    def sort(self):
        # Sorts the various classes into the groups and the
        pass

    def show_timetable(self):
        # return the object in a single nested dictionary of the format {"grade":{timetable}}
        pass

    def comparision_operator(self):
        # makes a comparable string so that the timetable can be compared with only a single parameter
        pass

    def make_other_case(self):
        # makes other case of timetable, other than the currently made timetable
        # each new case would have a new comparision operator too
        pass
