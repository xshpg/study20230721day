from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import UniqueValidator

from projects.serializer import ProjectModelSerializer
from interfaces.models import Interfaces


class InterfaceModelSerializer(serializers.ModelSerializer):
    project = ProjectModelSerializer(label='所属项目',write_only=True)

    class Meta:
        model = Interfaces
        fields = '__all__'







































