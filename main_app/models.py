from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
    ordering =['complete']

class SubTask(models.Model):
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  task = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  class Meta:
    ordering =['complete']