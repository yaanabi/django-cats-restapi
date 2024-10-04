from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(verbose_name='Cat name', max_length=255)
    description = models.TextField(verbose_name='Cat description',
                                   max_length=500)
    age = models.PositiveSmallIntegerField(verbose_name='Age in full months')
    color = models.CharField(verbose_name='Cat color', max_length=100)
    owner = models.ForeignKey(User,
                              verbose_name='Cat\'s owner',
                              on_delete=models.CASCADE,
                              related_name='cats_for_owner',
                              default=0)
    breed = models.ForeignKey(Breed,
                              on_delete=models.CASCADE,
                              related_name='cats_for_breed')

    def __str__(self):
        return self.name


class CatRating(models.Model):
    rating = models.IntegerField(verbose_name='Rating in range from 1 to 5', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5,
                                                                           5)])
    cat = models.ForeignKey(Cat,
                            on_delete=models.CASCADE,
                            related_name='cat_ratings')
    rated_by_user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_rated')
    
    class Meta:
        unique_together = ('cat', 'rated_by_user')

    def __str__(self) -> str:
        return f'Rating for {self.cat.name} by {self.rated_by_user.username}'