import django_filters
from django.db.models import Q
from .models import Book, Journal

class BookFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_title_or_author', label='Search Title or Author')
    
    class Meta:
        model = Book
        fields = {
            'status' : ['exact'],
            'genre' : ['exact'],
        }
        
    def filter_title_or_author(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(author__icontains=value)
        )
        
class StatusFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'status' : ['exact'],
        }
        
class JournalFilter(django_filters.FilterSet):
    class Meta:
        model = Journal
        fields = {
            'book__title' : ['icontains'],
            'mood' : ['exact'],
        }