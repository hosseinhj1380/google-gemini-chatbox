from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from rest_framework.views import APIView , Response , status
from .serializers import ChatSerializer
from drf_yasg.utils import swagger_auto_schema
from core.google_connection import GenAi
from django.http import StreamingHttpResponse
from rest_framework.decorators import action





class RestApiChat(APIView):
    serializer_class = ChatSerializer
    
    @swagger_auto_schema(
        operation_description="redirect ", request_body=ChatSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = ChatSerializer(data =request.data)
        if serializer.is_valid():
            obj = GenAi()
            response =obj.chat(message=serializer.validated_data["message"])
            print(response)
            return Response({"response":response},status=status.HTTP_200_OK)
        
        
        
class StreamChat(APIView):
    serializer_class = ChatSerializer
    
    @swagger_auto_schema(
        operation_description="redirect ", request_body=ChatSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = ChatSerializer(data =request.data)
        if serializer.is_valid():
            
            obj = GenAi()
            responses =obj.stream_chat(message=serializer.validated_data["message"])
            response = StreamingHttpResponse(responses, content_type="text/plain")
            # response['Cache-Control']= 'no-cache'
            # response['Content-Disposition'] = 'attachment; filename="streamed_response.txt"'
            return response
