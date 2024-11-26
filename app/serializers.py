from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name','language']

class AgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id','name','language','voice_id','updated']


class CampaignSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(many=True, queryset=Agent.objects.all())

    class Meta:
        model = Campaign
        fields = "__all__"


class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = ['name', 'type', 'phone', 'cost', 'outcome', 'call_duration', 'recording', 'summary', 'transcription', 'campaign']


class CampaignResultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = ['id','name', 'type', 'phone', 'cost', 'outcome', 'call_duration', 'recording', 'summary', 'transcription', 'campaign']
