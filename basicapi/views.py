from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializers
from .models import Note

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
