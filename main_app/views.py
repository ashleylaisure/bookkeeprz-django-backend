from .models import *
from rest_framework import permissions, viewsets
from .serializers import *
from rest_framework.response import Response


# Create your views here.

# --------------------------------  Books
class BookViewset(viewsets.ViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    
    def list(self, request):
        queryset = Book.objects.all()
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