from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Jot(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('jots_index')

  class Meta:
    ordering =['complete']

class SubJot(models.Model):
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  jot = models.ForeignKey(Jot, related_name="subjots", on_delete=models.CASCADE)

  def __str__(self):
    return '%s - %s' % (self.jot.title, self.title)

  def get_absolute_url(self):
    return reverse('jots_detail', kwargs={'jot_id': self.jot.id})

  class Meta:
    ordering =['complete']