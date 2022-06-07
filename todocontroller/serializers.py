from todocontroller.models import TodoController
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoController
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(TodoSerializer, self).to_representation(instance)
        representation['user']  = instance.user.username
        return representation
