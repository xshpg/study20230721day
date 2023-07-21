from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='确认密码',min_length=6,max_length=20,
                                             help_text='确认密码',write_only=True,error_messages={
            'min_length':'6-20之间',
            'max_length':'6-20之间'
        })
    token = serializers.CharField(label='生成token',read_only=True)

    class Meta:
        model = User
        fields = ('id','username','password','email','password_confirm','token')
        extra_kwargs = {
            'username':{
                'label':'用户名',
                'help_text':'用户名',
                'min_length':6,
                'max_length':20,
                'error_messages':{
                    'min_length':'6-20位数',
                    'max_length':'60-20位数'
                }
            },
            'password':{
                'label':'密码',
                'help_text':'密码',
                'min_length':6,
                'max_length':20,
                'error_messages':{
                    'min_length':'6-20位数',
                    'max_length':'6-20位数'
                }
            },
            'email':{
                'label':'邮箱',
                'help_text':'邮箱',
                'min_length':6,
                'max_length':20,
                'write_only':True,
                'required':True,
                'validators':[UniqueValidator(queryset=User.objects.all(),message='邮箱已注册')],
                'error_messages':{
                    'min_length':'6-20位数',
                    'max_length':'6-20位数'
                }
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password_confirm != password:
            raise serializers.ValidationError('密码不一致')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user




















