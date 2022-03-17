from rest_framework import generics
from .serializer import CountrySerializer
from .models import Country

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class CountryList(generics.ListCreateAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer


