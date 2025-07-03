from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .filters import BookFilter, StatusFilter


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
    fields = '__all__'
    template_name = "books/book_form.html"
    
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "books/book_form.html"
    
class BookDelete(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = '/books/'
