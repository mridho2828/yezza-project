from rest_framework import serializers
from rest_framework.fields import ListField
from .models import Note


class StringArrayField(ListField):
    def to_representation(self, obj):
        obj = super().to_representation(obj)
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        return super().to_internal_value(data)


class NoteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    attachments = StringArrayField()
