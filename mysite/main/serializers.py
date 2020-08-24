from rest_framework import serializers
from main.models import Tutorial

#Tutorial Serializer

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'