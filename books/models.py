from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image


class Category(models.Model):
    name = models.CharField(max_length=50)
class Book(models.Model):

    status_book = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True, blank=True)
    photo_author = models.FileField(  max_length=100, upload_to='bookfile',null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Road(models.Model):
    city1 = models.ForeignKey(City, related_name='city1_roads', on_delete=models.CASCADE)
    city2 = models.ForeignKey(City, related_name='city2_roads', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.city1} - {self.city2}: {self.distance} km"

    class Meta:
        unique_together = ('city1', 'city2')