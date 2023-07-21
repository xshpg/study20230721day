from rest_framework import serializers

from scholars.models import Scholars


class ScholarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholars
        fields = ('id','name','gender','age','address','education_level','edu_type','personal_experience')

    def create(self, validated_data):
        return Scholars.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.gender = validated_data['gender']
        instance.address = validated_data['address']
        instance.education_level = validated_data['education_level']
        instance.edu_type = validated_data['edu_type']
        instance.personal_experience = validated_data['personal_experience']
        instance.save()
        return instance