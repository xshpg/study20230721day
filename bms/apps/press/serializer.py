from rest_framework import serializers

from press.models import Press


class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        exclude = ('is_delete','update_time')
        extra_kwargs = {
            'create_time':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        return Press.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.desc = validated_data['desc']
        instance.save()
        return instance