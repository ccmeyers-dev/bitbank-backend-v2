from smtplib import SMTPException
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Account


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # add custom claim
        token['email'] = user.email
        return token


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True),
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    region = serializers.CharField()
    gender = serializers.CharField()
    referrer = serializers.CharField(allow_null=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name',
                  'region', 'gender', 'referrer', 'password')
        extra_kwargs = {
            'referrer': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same you can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.password2 = password
        instance.save()
        return instance
