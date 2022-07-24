from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Musician(models.Model):
    artistName = models.CharField(max_length=25)
    type = models.CharField(max_length=15)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.artistName


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    albumName = models.CharField(max_length=20)
    releaseDate = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
    score = (
        (0, 'Not Good'),
        (1, 'Not Bad'),
        (2, 'Ok'),
        (3, 'Good'),
        (4, 'Cool'),
        (5, 'Awesome')
    )
    rating = models.IntegerField(choices=score)

    def __str__(self):
        return self.artist + " " + self.albumName + " " + str(self.rating)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
