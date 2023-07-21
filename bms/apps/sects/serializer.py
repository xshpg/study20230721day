from rest_framework import serializers

from sects.models import Sects


class SectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sects
        fields = ('id','name','creat_user','desc')
        extra_kwargs = {}

    def create(self, validated_data):
        return Sects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.creat_user = validated_data['creat_user']
        instance.desc = validated_data['desc']
        instance.save()
        return instance