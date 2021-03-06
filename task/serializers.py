from rest_framework import serializers

from .models import Fact

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['fact']
        ready_only_fields = fields
        