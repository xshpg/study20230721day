from rest_framework import serializers

from martails.models import Martails


class MartailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Martails
        exclude = ('is_delete','update_time')
        extra_kwargs = {
            'create_time':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        return Martails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.people = validated_data['people']
        instance.learn_time = validated_data['learn_time']
        instance.power_value = validated_data['power_value']
        instance.desc = validated_data['desc']
        instance.save()
        return instance