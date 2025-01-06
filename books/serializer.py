from rest_framework import serializers 
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=['title','author','genre','publication_year','available_copies','isbn_number','rating']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance