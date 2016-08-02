from django.db import models

# Create your models here.
class Question(models.Model):
    test = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now=True)

class Choice(models.Model):
    questionRelation = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)