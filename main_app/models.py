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

MOOD_CHOICES = (
    ('anxious', 'Anxious'),
    ('calm', 'Calm'),
    ('cheerful', 'Cheerful'),
    ('depressing','Depressing'),
    ('eerie','Eerie'),
    ('festive','Festive'),
    ('foreboding','Foreboding'),
    ('frightening','Frightening'),
    ('frustrated','Frustrated'),
    ('gloomy','Gloomy'),
    ('hopeless','Hopeless'),
    ('humorous','Humorous'),
    ('idyllic','Idyllic'),
    ('joyful','Joyful'),
    ('light-hearted','Light-hearted'),
    ('lonely','Lonely'),
    ('mlancholic','Melancholic'),
    ('mysterious','Mysterious'),
    ('ominous','Ominous'),
    ('optimistic','Optimistic'),
    ('panicked','Panicked'),
    ('peaceful','Peaceful'),
    ('pensive','Pensive'),
    ('pessimistic','Pessimistic'),
    ('reflective','Reflective'),
    ('romantic','Romantic'),
    ('sad','Sad'),
    ('sentimental','Sentimental'),
    ('stressed','Stressed'),
    ('suspenseful','Suspenseful'),
    ('tense','Tense'),
    ('uneasy','Uneasy'),
    ('uplifting','Uplifting'),
    ('whimsical','Whimsical'),
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
    

class Journal(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(max_length=250)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, blank=True, null=True)
    chapter = models.CharField(max_length=100, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Journal entry for {self.book.title} added on {self.date_added}"
    
    class Meta:
        ordering = ['-date']