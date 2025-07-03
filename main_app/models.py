from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    ('tbr' , 'TBR'),
    ('reading', 'Reading'),
    ('read', 'Read'),
    ('paused', 'Paused'),
    ('dnf', 'DNF')
)

FORMAT_CHOICES = (
    ('audio', 'Audiobook'),
    ('ebook', 'eBook'),
    ('physical', 'Physical Book')
)

GENRE_CHOICES = (
    ('biography', 'Biography'), 
    ('classic' ,'Classic'), 
    ('contemporary_fiction' ,'Contemporary Fiction'), 
    ('dark_academia', 'Dark Academia'), 
    ('fantasy', 'Fantasy'), 
    ('historical_fiction', 'Historical Fiction'), 
    ('history', 'History'), 
    ('horror', 'Horror'), 
    ('literary_fiction', 'Literary Fiction'), 
    ('memoir', 'Memoir'), 
    ('mystery', 'Mystery'), 
    ('nonfiction', 'Nonfiction'), 
    ('play', 'Play'), 
    ('poetry', 'Poetry'), 
    ('retelling', 'Retelling'),
    ('romance', 'Romance'), 
    ('romantasy', 'Romantasy'), 
    ('science_fiction', 'Science Fiction'),
    ('thriller', 'Thriller'), 
    ('young_adult', 'Young Adult'),
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=250, blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='tbr')
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    publication_year = models.IntegerField(blank=True, null=True)
    total_pages = models.IntegerField(blank=True, null=True)
    total_time = models.DurationField(blank=True, null=True)
    re_read = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"book_id": self.id})
    