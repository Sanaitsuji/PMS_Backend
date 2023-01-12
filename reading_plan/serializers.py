from rest_framework import serializers
from .models import Technology, CharacterHated, CharacterLoved, UnimpressiveSections

class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = ('id', 'name', 'description', 'used_by', 'draw')
        read_only_fields = ('created_at',)

class CharacterHatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterHated
        fields = ('id', 'name', 'description')
        read_only_fields = ('created_at',)

class CharacterLovedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterLoved
        fields = ('id', 'name', 'description')
        read_only_fields = ('created_at',)

class UnimpressiveSectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnimpressiveSections
        fields = ('id', 'name', 'description')
        read_only_fields = ('created_at',)
