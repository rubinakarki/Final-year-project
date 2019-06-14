from django.db import models

# Create your models here.
class Songs(models.Model):
    name = models.CharField(max_length=100,null = True,blank = True)
    link_of_song  = models.URLField(max_length = 100)
    artist = models.CharField(max_length=100,null = True,blank = True)
    genre =  models.CharField(max_length = 100)
    angry = models.PositiveIntegerField()
    disgust = models.PositiveIntegerField()
    fear = models.PositiveIntegerField()
    happy = models.PositiveIntegerField()
    neutral = models.PositiveIntegerField()
    sad = models.PositiveIntegerField()
    surprise = models.PositiveIntegerField()
    
    def __str__(self):
        return  f'{self.name}  by  {self.artist}'