from rest_framework import generics
from .serializer import CountrySerializer
from .models import Country
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class CountryList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Country.objects.all()
  serializer_class = CountrySerializer


