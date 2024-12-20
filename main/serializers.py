from rest_framework import serializers
from .models import SpyCat, Mission, Target
import requests

CAT_API_URL = "https://api.thecatapi.com/v1/breeds"


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes', 'completed']

    def validate_notes(self, value):
        if self.instance and self.instance.completed:
            raise serializers.ValidationError("Cannot change notes for a completed target.")
        return value


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'completed', 'targets']

    def validate_notes(self, value):
        if self.instance and self.instance.completed:
            raise serializers.ValidationError("Cannot change notes for a completed target.")
        return value


class MissionWithTargetsSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['cat', 'completed', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission

    def validate(self, data):
        if 'targets' in data:
            for target in data['targets']:
                if target.get('completed') and 'notes' in target:
                    raise serializers.ValidationError("Cannot modify notes for completed targets.")
        return data


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'experience_years', 'breed', 'salary']

    def validate_breed(self, value):
        response = requests.get(CAT_API_URL)
        if response.status_code != 200:
            raise serializers.ValidationError("Error fetching breed data from TheCatAPI.")

        breeds = response.json()
        breed_names = [breed['name'].lower() for breed in breeds]

        if value.lower() not in breed_names:
            raise serializers.ValidationError(f"The breed '{value}' is not valid. Please check the breed name.")

        return value
