from django.db import models
from django.contrib.auth.models import User

# models
class Topic(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Book(models.Model):
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
  name = models.CharField(max_length=200)
  topic = models.CharField(max_length=200, null=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated','-created']
  def __str__(self):
    return self.name

class Note(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  title = models.CharField(max_length=200)
  body = models.TextField(null=True, blank=True)
  book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now = True)

  class Meta:
    ordering = ['-updated','-created']

    def __str__(self):
      return self.body[0:50]