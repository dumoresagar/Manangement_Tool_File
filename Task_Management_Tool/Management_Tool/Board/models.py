from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class Board(models.Model):
    Board_Name = models.IntegerField()
    Color = ColorField(default='#FF0000')


    def __str__(self):
        return self.Board_Name

status = (('to do','To do'),('in progress','In Progress'),('on hold','On Hold'),('complated','Complated'),('released','Released'))
class Task(models.Model):
    Board_id = models.OneToOneField(Board, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    current_status = models.CharField(max_length=200,choices=status)

    def __str__(self):
        return f"{self.Board_id},{self.task_name},{self.current_status}"