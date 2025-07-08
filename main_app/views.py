from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Journal
from .filters import BookFilter, StatusFilter, JournalFilter
from .forms import BookForm


from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# --------------------------------  User
# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

# --------------------------------  Books
class BookViewset(viewsets.ViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        book = self.queryset.get(pk=pk)
        serializer = self.serializer_class(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        book = self.queryset.get(pk=pk)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        book = self.queryset.get(pk=pk)
        book.delete()
        return Response(status=204)
    
    

# class BookListCreate(generics.ListCreateAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Book.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class BookDelete(generics.DestroyAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Book.objects.filter(user=self.request.user)
    
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Book.objects.filter(user=self.request.user)

# # book index - search
# def book_index(request):
#     book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    
#     context = {
#         'form' : book_filter.form,
#         'books' : book_filter.qs
#     }
#     return render(request, 'books/index.html', context )

# # book index - by status
# def book_index_status(request):
#     get_data = request.GET.copy()
    
#     if 'status' not in get_data:
#         get_data['status'] = 'reading'
        
#     book_filter = StatusFilter(get_data, queryset=Book.objects.all())
    
#     context = {
#         'form' : book_filter.form,
#         'books' : book_filter.qs,
#         'active_status' : get_data.get('status'),
#     }
    
#     return render(request, 'books/index_status.html', context)

# def book_detail(request, book_id):
#     book = Book.objects.get(id=book_id)
#     return render(request, 'books/detail.html', {'book' : book})

# class BookCreate(CreateView):
#     model = Book
#     form_class = BookForm
#     template_name = "books/book_form.html"
    
# class BookUpdate(UpdateView):
#     model = Book
#     form_class = BookForm
#     template_name = "books/book_form.html"
    
# class BookDelete(DeleteView):
#     model = Book
#     template_name = "books/book_confirm_delete.html"
#     success_url = '/books/'
    
# # --------------------------------  Journal
# def journal_index(request, book_id):
#     book = Book.objects.get(id=book_id)
#     journals = book.journal_set.all()
    
#     return render(request, 'journal/index.html', {
#         'book' : book,
#         'journals' : journals,
#     })
    
# class JournalCreate(CreateView):
#     model = Journal
#     fields = ['title', 'notes', 'mood', 'chapter', 'page']
#     template_name = 'journal/journal_form.html'
    
#     def form_valid(self, form):
#         book = get_object_or_404(Book, pk=self.kwargs['book_id'])
#         form.instance.book = book
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('journal-index', kwargs={'book_id': self.kwargs['book_id']})
    

# def journal_detail(request, journal_id):
#     journal = Journal.objects.get(id=journal_id)
#     return render(request, 'journal/detail.html', {'journal' : journal })

# class JournalUpdate(UpdateView):
#     model = Journal
#     fields = ['title', 'notes', 'mood', 'chapter', 'page']
#     template_name = "journal/journal_form.html"
    
# class JournalDelete(DeleteView):
#     model = Journal
#     template_name = "journal/journal_confirm_delete.html"
    
#     def get_success_url(self):
#         book_id = self.object.book.id 
#         return reverse('journal-index', kwargs={'book_id' : book_id})
    
# # --------------------------------  Journal All
# def journal_index_all(request):
#     journal_filter = JournalFilter(request.GET, queryset=Journal.objects.all())

#     return render(request, 'journal/index_all.html', { 
#         'form' : journal_filter.form,
#         'journal' : journal_filter.qs,
#         } )
    
# class NewJournalCreate(CreateView):
#     model = Journal
#     fields = ['title', 'notes', 'mood', 'chapter', 'page', 'book']
#     template_name = 'journal/journal_form.html'
    
#     def get_success_url(self):
#         return reverse('journal-index', kwargs={'book_id': self.object.book.id})
    
# --------------------------------  Bookshelves
# class BookshelfCreate(CreateView):
#     model = Bookshelf
#     fields = '__all__'
#     template_name = "bookshelves/bookshelf_form.html"


    
# def bookshelf_detail(request, bookshelf_id):
#     bookshelf = Bookshelf.objects.get(id=bookshelf_id)
#     return render(request, 'bookshelves/detail.html', {'bookshelf' : bookshelf })

# class BookshelfUpdate(UpdateView):
#     model = Bookshelf
#     fields = '__all__'
#     template_name = "bookshelves/bookshelf_form.html"
    
# class BookshelfDelete(DeleteView):
#     model = Bookshelf
#     template_name = "bookshelves/bookshelf_confirm_delete.html"
#     success_url = '/bookshelves/'
    
    
# def bookshelf_index(request):
#     bookshelves = Bookshelf.objects.all()

#     book_filter = BookshelfFilter(request.GET, queryset=Book.objects.all())
    
#     context = {
#         'form' : book_filter.form,
#         'books' : book_filter.qs,
#         'active_bookshelf' : int(request.GET.get('bookshelf')) if request.GET.get('bookshelf') else None,
#         'bookshelves' : bookshelves
#     }
    
#     return render(request, 'bookshelves/index.html', context)