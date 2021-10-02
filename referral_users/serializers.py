from rest_framework import serializers
from .models import ReferralUser, FormResults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'referral_code')
        model = ReferralUser


class FormResultsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('chat_id', 'tg_username', 'name', 'phone_number', 'answers')
        model = FormResults
