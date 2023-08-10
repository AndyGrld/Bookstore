from django.db import models

from authentication.models import Profile


# Create your models here.
class Genre(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Biography', 'Biography'),
        ('Self-Help', 'Self-Help'),
    ]
    name = models.CharField(max_length=25, choices=GENRE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    RATED = [
        ('E', 'Everyone'),
        ('T', 'Teen'),
        ('M', 'Mature'),
        ('R', 'Restricted'),
    ]

    author = models.ForeignKey(Profile, related_name='book_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='book_cover/', null=True, blank=True)
    book = models.FileField(upload_to='books/')
    description = models.TextField()
    downloads = models.PositiveIntegerField(default=0)
    ratings = models.PositiveIntegerField(default=0)
    downloaded_books = models.ManyToManyField(Profile, related_name='downloaded_by', blank=True)
    favorited_by = models.ManyToManyField(Profile, related_name='favorite_books', blank=True)
    rated = models.CharField(max_length=1, choices=RATED)
    date_published = models.DateField(auto_created=True, auto_now_add=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return str(self.title[:20])


class Review(models.Model):
    author = models.ForeignKey(Profile, related_name='author_review', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_review', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.author.user.username} for {self.book.title}"


