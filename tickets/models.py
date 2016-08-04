from django.db import models

# Create your models here.
class Ticket(models.Model):
    
    statusMap = (
        (1, "Waiting" ),
        (2,"Approved"),
        (3,"In progress"),
        (4,"Completed"),
        (5,"Rejected"),
    )
    
    requesterName = models.CharField(max_length=50)
    requestDate = models.DateTimeField(auto_now=True)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    requesterEmail = models.EmailField()
    requestedEmail = models.EmailField()
    comment = models.CharField(max_length=300)
    status = models.IntegerField(default=1,choices=statusMap)
    #chatID
    