from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, AgentListSerializer, CampaignResultSerializer, CampaignResultListSerializer


class AgentAPIView(APIView):


    def post(self, request):
        
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        agent =  Agent.objects.get(id=pk)
        if not agent:
            return Response({"error": "Agent not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AgentSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgentDetailAPIView(APIView):

    def get(self, request, pk):
        agent = Agent.objects.get(id=pk)
        if not agent:
            return Response({"error": "Agent not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AgentSerializer(agent)
        return Response(serializer.data)

class AgentDeleteAPIView(APIView):
    def delete(self, request, pk):
        agent = Agent.objects.get(id=pk)
        if not agent:
            return Response({"error": "Agent not found."}, status=status.HTTP_404_NOT_FOUND)
        agent.delete()
        return Response({"message": "Agent deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class AgentListView(APIView):
    
        def get(self, request):
        
            page_size = int(request.query_params.get("page_size", 10))
            page_number = int(request.query_params.get("page", 1))

            agents = Agent.objects.all()
            paginator = Paginator(agents, page_size)
            page = paginator.get_page(page_number)

            serializer = AgentListSerializer(page.object_list, many=True)
            return Response({
                "count": paginator.count,
                "num_pages": paginator.num_pages,
                "results": serializer.data,
            })
        
        
class CampaignListAPIView(APIView):


    def get(self, request):

        page_size = int(request.query_params.get("page_size", 10))
        page_number = int(request.query_params.get("page", 1))

        campaigns = Campaign.objects.all()
        paginator = Paginator(campaigns, page_size)
        page = paginator.get_page(page_number)

        serializer = CampaignSerializer(page.object_list, many=True)
        return Response({
            "count": paginator.count,
            "num_pages": paginator.num_pages,
            "results": serializer.data,
        })

class CampaingAPIView(APIView):
    
    def post(self, request):

        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        campaign = Campaign.objects.get(id=pk)
        if not campaign:
            return Response({"error": "Campaign not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CampaignSerializer(campaign, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignDetailAPIView(APIView):
        
    def get(self, request, pk):
        campaign = Campaign.objects.get(id=pk)
        if not campaign:
            return Response({"error": "Campaign not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)
    
class CampaignDeleteAPIView(APIView):
    
    def delete(self, request, pk):
        campaign = Campaign.objects.get(id=pk)
        if not campaign:
            return Response({"error": "Campaign not found."}, status=status.HTTP_404_NOT_FOUND)
        campaign.delete()
        return Response({"message": "Campaign deleted successfully."}, status=status.HTTP_204_NO_CONTENT)





### Campaign Result API's View

class CampaignResultListAPIView(APIView):

    def get(self, request):
        page_size = int(request.query_params.get("page_size", 10))
        page_number = int(request.query_params.get("page", 1))

        campaign_results = CampaignResult.objects.all()
        paginator = Paginator(campaign_results, page_size)
        page = paginator.get_page(page_number)

        serializer = CampaignResultListSerializer(page.object_list, many=True)
        return Response({
            "count": paginator.count,
            "num_pages": paginator.num_pages,
            "results": serializer.data,
        })
        
        

class CampaignResultAPIView(APIView):
    """
    API for creating and updating campaign results.
    """

    def post(self, request):

        serializer = CampaignResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        try:
            campaign_result = CampaignResult.objects.get(id=pk)
        except CampaignResult.DoesNotExist:
            return Response({"error": "Campaign result not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CampaignResultSerializer(campaign_result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

class CampaignResultDetailAPIView(APIView):


    def get(self, request, pk):

        try:
            campaign_result = CampaignResult.objects.get(id=pk)
        except CampaignResult.DoesNotExist:
            return Response({"error": "Campaign result not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CampaignResultSerializer(campaign_result)
        return Response(serializer.data)

    def delete(self, request, pk):

        try:
            campaign_result = CampaignResult.objects.get(id=pk)
        except CampaignResult.DoesNotExist:
            return Response({"error": "Campaign result not found."}, status=status.HTTP_404_NOT_FOUND)

        campaign_result.delete()
        return Response({"message": "Campaign result deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
