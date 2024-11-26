from django.db import models
import uuid

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.UUIDField(default=uuid.uuid4, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    
    CAMPAIGN_TYPES = (
        ('INB', 'Inbound'),
        ('OBD', 'Outbound'),
    )
    
    CAMPAIGN_STATUSES = (
        ('RUN', 'Running'),
        ('PAU', 'Paused'),
        ('COM', 'Completed'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=50, choices=CAMPAIGN_STATUSES)
    agents = models.ManyToManyField(Agent, related_name="campaigns")

    def __str__(self):
        return self.name

class CampaignResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="results")

    def __str__(self):
        return self.name
