from rest_framework import serializers

from editors.models import Editors


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editors
        exclude = ('update_time','is_delete')
        extra_kwargs = {
            'create_time':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        return Editors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.gender = validated_data['gender']
        instance.age = validated_data['age']
        instance.address = validated_data['address']
        instance.desc = validated_data['desc']
        instance.save()
        return instance
