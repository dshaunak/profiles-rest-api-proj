from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field from testing our API View"""
    name = serializers.CharField(max_length=15)
