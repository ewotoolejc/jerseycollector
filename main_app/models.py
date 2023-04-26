from django.db import models
from django.urls import reverse

# Create your models here.
class Hat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    team_name = models.CharField(max_length=50)
    picture = models.URLField()
    
    def __str__(self):
       return self.name

    def get_absolute_url(self):
        return reverse('hat_details', args=[str(self.id)])

class Jersey(models.Model):
    jersey_name = models.CharField(max_length=50, default='My New Jersey')
    team_name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    year = models.DateField()
    description = models.TextField(max_length=500)
    picture = models.URLField()
    hats = models.ManyToManyField(Hat)

    def __str__(self):
        return self.team_name
    
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    dry_cleaned = models.BooleanField(blank=False)

    jersey = models.ForeignKey(Jersey, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cleaned on {self.date}"

    