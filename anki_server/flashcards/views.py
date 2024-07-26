from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardListCreate(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
