from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "requesterName",
            "requesterEmail",
            "requestedEmail",
            "comment",
            "status",
        ]
    