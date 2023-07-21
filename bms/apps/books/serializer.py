from rest_framework import serializers

from books.models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        exclude = ('is_delete','update_time')
        extra_kwargs = {
            'create_time':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.author = validated_data['author']
        instance.press = validated_data['press']
        instance.press_time = validated_data['press_time']
        instance.desc = validated_data['desc']
        instance.save()
        return instance
