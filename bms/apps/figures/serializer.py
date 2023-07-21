from rest_framework import serializers

from figures.models import Figures


class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figures
        exclude = ('is_delete','update_time')
        extra_kwargs = {
            'create_time':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        return Figures.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.title = validated_data['title']
        instance.nation = validated_data['nation']
        instance.desc = validated_data['desc']
        instance.save()
        return instance