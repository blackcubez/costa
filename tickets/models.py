from django.db import models

# Create your models here.
class Ticket(models.Model):
    requesterName = models.CharField(max_lenth=50)
    requestDate = models.DateTimeField(auto_now=True)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    emailRequester = models.EmailField()
    requestedEmail = models.EmailField()
    comment = models.CharField(max_length=300)
    secretID = models.CharField(max_length=64) #SHA512
    #chatID
    