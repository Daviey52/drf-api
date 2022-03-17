from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id','organization','name','continent','added_at','updated_at')
    model = Country
