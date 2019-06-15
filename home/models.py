from django.db import models

# Create your models here.
class Songs(models.Model):
    name = models.CharField(max_length=100,null = True,blank = True)
    link_of_song  = models.URLField(max_length = 100)
    artist = models.CharField(max_length=100,null = True,blank = True)
    genre =  models.CharField(max_length = 100)
    angry = models.DecimalField(max_digits=5, decimal_places=2)
    disgust = models.DecimalField(max_digits=5, decimal_places=2)
    fear = models.DecimalField(max_digits=5, decimal_places=2)
    happy = models.DecimalField(max_digits=5, decimal_places=2)
    neutral =models.DecimalField(max_digits=5, decimal_places=2)
    sad = models.DecimalField(max_digits=5, decimal_places=2)
    surprise = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return  f'{self.name}  by  {self.artist}'

        