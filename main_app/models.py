from django.db import models
from django.urls import reverse

# Create your models here.
class Jersey(models.Model):
    jersey_name = models.CharField(max_length=50, default='My New Jersey')
    team_name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    year = models.DateField()
    description = models.TextField(max_length=500)
    picture = models.URLField()

    def __str__(self):
        return self.team_name
    
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

