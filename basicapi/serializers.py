from rest_framework import serializers
from rest_framework.fields import ListField
from .models import Note


class NoteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    attachments = ListField()
