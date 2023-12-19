from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    @classmethod
    def to_entity(self):
        pass
