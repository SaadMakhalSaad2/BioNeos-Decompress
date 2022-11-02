from rest_framework import serializers
from . models import MessageData

class MessageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageData
        field = '__all__'