from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
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

    def perform_destroy(self, instance):
        instance = model_to_dict(instance)
        author = instance['author']
        user = self.request.user
        if author != user:
            raise PermissionDenied({
                "message": "You don't have permission to perform this request"
            })

        return super().perform_destroy(instance)

    def perform_update(self, serializer):
        author = serializer.validated_data.get('author')
        user = self.request.user
        if author != user:
            raise PermissionDenied({
                "message": "You don't have permission to perform this request"
            })

        return super().perform_update(serializer)
