from rest_framework import serializers
from .models import *


class HeroSectionSerial(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class CompanySerial(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class PresidentSerial(serializers.ModelSerializer):
    class Meta:
        model = PresidentSpeech
        fields = '__all__'


class AboutSerial(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactSerial(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class TermsSerial(serializers.ModelSerializer):
    class Meta:
        model = TermsofService
        fields = '__all__'


class PoliciesSerial(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'


class GallerySerial(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class StaffsSerial(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'


class AnnounceSerial(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = '__all__'


class ConferenceSerial(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'


class FooterSerial(serializers.ModelSerializer):
    contacts = ContactSerial(many=False, required=False)
    policies = PoliciesSerial(many=False, required=False)
    termsofService = TermsSerial(many=False, required=False)

    class Meta:
        model = Footer
        fields = '__all__'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', None)
        policies_data = validated_data.pop('policies', None)
        termsofService_data = validated_data.pop('termsofService', None)

        footer = Footer.objects.create(**validated_data)

        if contacts_data:
            Contacts.objects.create(footer=footer, **contacts_data)
        if policies_data:
            Policies.objects.create(footer=footer, **policies_data)
        if termsofService_data:
            TermsofService.objects.create(footer=footer, **termsofService_data)

        return footer

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', None)
        policies_data = validated_data.pop('policies', None)
        termsofService_data = validated_data.pop('termsofService', None)

        instance = super().update(instance, validated_data)

        if contacts_data:
            Contacts.objects.filter(footer=instance).update(**contacts_data)
        if policies_data:
            Policies.objects.filter(footer=instance).update(**policies_data)
        if termsofService_data:
            TermsofService.objects.filter(
                footer=instance).update(**termsofService_data)

        return instance
