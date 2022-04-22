from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NoteSerializers
from .models import Note

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )
    filter_fields = (
        'author',
    )
    search_fields = (
        'text',
    )
