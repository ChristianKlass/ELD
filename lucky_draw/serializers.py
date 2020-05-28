from rest_framework import serializers
from lucky_draw.models import Contestant, Event, Draw, Prize


class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contestant
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class DrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draw
        fields = '__all__'


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'

