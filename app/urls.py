from django.urls import path
from .views import AgentListView, AgentDetailAPIView, AgentAPIView, AgentDeleteAPIView,CampaignListAPIView, CampaingAPIView, CampaignDetailAPIView, CampaignDeleteAPIView, CampaignResultAPIView, CampaignResultListAPIView, CampaignResultDetailAPIView

urlpatterns = [
    path('list-agents/', AgentListView.as_view(), name='agent-list'),  # List agents with pagination
    path('agents/<uuid:pk>/', AgentDetailAPIView.as_view(), name='agent-detail'),  # Get a single agent
    path('agents/delete/<uuid:pk>/',AgentDeleteAPIView.as_view(), name='agent-delete'),  # delete a single agent
    path('agents/create/', AgentAPIView.as_view(), name='agent-create'),  # Create an agent
    path('agents/update/<uuid:pk>/', AgentAPIView.as_view(), name='agent-update'),  # Update an agent
    

    path('list-campaigns/', CampaignListAPIView.as_view(), name='campaign-list'),  # List all campaigns with pagination
    path('campaigns/create/', CampaingAPIView.as_view(), name='campaign-create'),  # Create a new campaign
    path('campaigns/update/<uuid:pk>/', CampaingAPIView.as_view(), name='campaign-update'),  # Create a new campaign
    path('campaigns/<uuid:pk>/', CampaignDetailAPIView.as_view(), name='campaign-detail'),  # Get,  delete a specific campaign
    path('campaigns/delete/<uuid:pk>/', CampaignDeleteAPIView.as_view(), name='campaign-delete'),  # Get, update, or delete a specific campaign
    
    
    path('campaign-results/', CampaignResultListAPIView.as_view(), name='campaign-result-list'),  # List all campaign results with pagination
    path('campaign-results/create/', CampaignResultAPIView.as_view(), name='campaign-result-create'),  # Create a new campaign result
    path('campaign-results/update/<uuid:pk>/', CampaignResultAPIView.as_view(), name='campaign-result-create'),  # Create a new campaign result
    path('campaign-results/<uuid:pk>/', CampaignResultDetailAPIView.as_view(), name='campaign-result-detail'),  # Retrieve, update, or delete a specific campaign result


]
