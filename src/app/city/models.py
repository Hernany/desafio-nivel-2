from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class State(models.Model):

    state_id = models.AutoFiel(primary_key=True, db_column='id')
    state_name = models.CharField(max_length=60, db_column='name')
    state_fu =  models.CharField(max_length=2, db_column='uf')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    state_status = models.BooleanField(default=False)

    def __str__(self):
        return self.state_name
    
    def save(self):
        self.state_status = True
        self.save()
    