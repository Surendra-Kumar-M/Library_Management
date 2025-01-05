from rest_framework import serializers 
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=['title','author','genre','publication_year','available_copies','isbn_number','rating']