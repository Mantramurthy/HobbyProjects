from django.db import models

# Create your models here.
class OnlineOp(models.Model):
    Gender_Choice=(('M', 'Male'),('F', 'Female'))
    #'choices' must be an iterable containing (actual value, human readable name) tuples.
    Timming_Choice=(('10:00-11:00','10:00-11:00'),
                    ('11:00-12:00','11:00-12:00'),
                    ('12:00-1:00','12:00-1:00'),
                    ('2:00-3:00','2:00-3:00'),
                    ('3:00-4:00','3:00-4:00'),
                    ('4:00-5:00','4:00-5:00'),)

    Patient_Name=models.CharField(max_length=20)
    Mobile = models.IntegerField()
    Age=models.IntegerField()
    #Gender=models.CharField(label='Gender', widget=models.Ra    RadioSelect,choices=Gender_Choice)
    Gender = models.CharField(choices=Gender_Choice, max_length=128)
    Timmings = models.CharField(max_length=11, choices=Timming_Choice, default="Select Timmings")

