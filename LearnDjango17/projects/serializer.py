from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import UniqueValidator

from projects.models import Projects


def is_unique_project_name(name):
    if '项目' not in name:
        raise validators.ValidationError('项目名需有项目')


class ProjectModelSerializer(serializers.ModelSerializer):
    interface_set = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'
        extra_kwargs = {
            'leader':{
                'write_only':True,
                'error_messages':{
                    'max_length':'不能超过50个字符',
                    'min_length':'不能小于6个字符'
                }
            },
            'name':{
                'write_only':True,
                'validators':[UniqueValidator(queryset=Projects.objects.all(),message='项目名唯一'),is_unique_project_name]
            }
        }

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance

    def validate_name(self,value):
        if not value.endswith('项目'):
            raise validators.ValidationError('以项目结尾')
        return value

    def validate(self, attrs):
        if 'amos' not in attrs['leader'] and 'amos' not in attrs['tester']:
            raise validators.ValidationError('负责人或者测试人需有amos')
        return attrs






































