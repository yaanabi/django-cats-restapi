from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Breed: self.name'

class Cat(models.Model):
    description = models.TextField(max_length=500)
    age = models.IntegerField(verbose_name='Age in full months')
    color = models.CharField(max_length=100)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='cats_for_user')
    breed = models.ForeignKey(Breed,
                              on_delete=models.CASCADE,
                              related_name='cats_for_breed')

    def __str__(self):
        return f'Cat: {self.name}, user: {self.user}'

class CatRating(models.Model):
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='cat_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rated')
    
