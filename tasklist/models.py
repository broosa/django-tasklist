from django.db import models
from django.contrib.auth.models import User

class base(models.Model):
    
    user = models.ForeignKey(User)
    time_due = models.DateTimeField()
    
    description = models.CharField(max_length=200)
    
    
    
