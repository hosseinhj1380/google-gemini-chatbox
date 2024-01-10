from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from rest_framework.views import APIView , Response , status
from .serializers import ChatSerializer
from drf_yasg.utils import swagger_auto_schema
from core.google_connection import GenAi






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
            response =obj.chat(message=serializer.validated_data["message"])
            print(response)
            return Response({"response":response},status=status.HTTP_200_OK)
