from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Journal
from .filters import BookFilter, StatusFilter, JournalFilter
from .forms import BookForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# --------------------------------  Books
# book index - search
def book_index(request):
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    
    context = {
        'form' : book_filter.form,
        'books' : book_filter.qs
    }
    return render(request, 'books/index.html', context )

# book index - by status
def book_index_status(request):
    get_data = request.GET.copy()
    
    if 'status' not in get_data:
        get_data['status'] = 'reading'

    book_status = StatusFilter(get_data, queryset=Book.objects.all())
    
    context = {
        'form' : book_status.form,
        'books' : book_status.qs,
        'active_status' : get_data['status']
    }
    
    return render(request, 'books/index_status.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book' : book})

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    
class BookDelete(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = '/books/'
    
# --------------------------------  Journal
def journal_index(request, book_id):
    book = Book.objects.get(id=book_id)
    journals = book.journal_set.all()
    
    return render(request, 'journal/index.html', {
        'book' : book,
        'journals' : journals,
    })
    
class JournalCreate(CreateView):
    model = Journal
    fields = ['title', 'notes', 'mood', 'chapter', 'page']
    template_name = 'journal/journal_form.html'
    
    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_id'])
        form.instance.book = book
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('journal-index', kwargs={'book_id': self.kwargs['book_id']})
    

def journal_detail(request, journal_id):
    journal = Journal.objects.get(id=journal_id)
    return render(request, 'journal/detail.html', {'journal' : journal })

class JournalUpdate(UpdateView):
    model = Journal
    fields = ['title', 'notes', 'mood', 'chapter', 'page']
    template_name = "journal/journal_form.html"
    
class JournalDelete(DeleteView):
    model = Journal
    template_name = "journal/journal_confirm_delete.html"
    
    def get_success_url(self):
        book_id = self.object.book.id 
        return reverse('journal-index', kwargs={'book_id' : book_id})
    
# --------------------------------  Journal All
def journal_index_all(request):
    journal_filter = JournalFilter(request.GET, queryset=Journal.objects.all())

    return render(request, 'journal/index_all.html', { 
        'form' : journal_filter.form,
        'journal' : journal_filter.qs,
        } )
    
class NewJournalCreate(CreateView):
    model = Journal
    fields = ['title', 'notes', 'mood', 'chapter', 'page', 'book']
    template_name = 'journal/journal_form.html'
    
    def get_success_url(self):
        return reverse('journal-index', kwargs={'book_id': self.object.book.id})