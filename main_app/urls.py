from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.BookViewset, basename='book' )
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name="about"), 
    
#     # Books 
#     # path('books/', views.BookListCreate.as_view(), name="book-index"),
#     # path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
#     # path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

#     # path('books/', views.book_index, name="book-index"),
#     path('books/status/', views.book_index_status, name="book-index-status"), 
#     path('books/<int:book_id>/', views.book_detail, name='book-detail'),
#     path('books/create/', views.BookCreate.as_view(), name="book-create"),
#     path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'), 
#     # path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    
#     # Journal (by Book)
#     path('books/<int:book_id>/journal/', views.journal_index, name="journal-index"),
#     path('books/<int:book_id>/journal/new/', views.JournalCreate.as_view(), name="journal-create"),
#     path('journal/<int:journal_id>/', views.journal_detail, name='journal-detail'), 
#     path('journal/<int:pk>/update/', views.JournalUpdate.as_view(), name='journal-update'),
#     path('journal/<int:pk>/delete/', views.JournalDelete.as_view(), name='journal-delete'), 
    
#     path('journal/', views.journal_index_all, name="journal-index-all"),
#     path('journal/new', views.NewJournalCreate.as_view(), name="new-journal-create"),
    
#     # Bookshelf
#     # path('bookshelves/', views.bookshelf_index, name="bookshelf-index"), 
#     # path('bookshelves/create/', views.BookshelfCreate.as_view(), name='bookshelf-create'), 
#     # path('bookshelves/<int:bookshelf_id>/', views.bookshelf_detail, name="bookshelf-detail"),
#     # path('bookshelves/<int:pk>/update/', views.BookshelfUpdate.as_view(), name="bookshelf-update"), 
#     # path('bookshelves/<int:pk>/delete/', views.BookshelfDelete.as_view(), name="bookshelf-delete"),
# ]
