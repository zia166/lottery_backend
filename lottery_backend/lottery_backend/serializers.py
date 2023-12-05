from rest_framework import serializers
from .models import Performance, LotteryEntry, Winner

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class LotteryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryEntry
        fields = '__all__'

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'