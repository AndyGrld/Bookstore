from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    genre = models.TextField(default='Not set')  # todo: change default
    bio = models.TextField(default='Not set')
    profilePic = models.ImageField(upload_to='profilePics/', null=True, blank=True)
    # interests = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='interests', blank=True)
    subscribers = models.ManyToManyField(User, related_name="subscribers", blank=True)
    subscribed_to = models.ManyToManyField(User, related_name="subscribed_to", blank=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def get_number_of_subscribers(self):
        return self.subscribers.count()

    @property
    def get_number_of_subscribed_to(self):
        return self.subscribed_to.count()

    @property
    def get_number_of_published_books(self):
        return self.book_author.count()
