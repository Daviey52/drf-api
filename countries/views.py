from rest_framework import generics
from .serializer import CountrySerializer
from .models import Country
from .permissions import IsOwnerOrReadOnly

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class CountryList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Country.objects.all()
  serializer_class = CountrySerializer


